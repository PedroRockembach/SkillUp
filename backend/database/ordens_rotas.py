from fastapi import APIRouter, Depends , HTTPException
from sqlalchemy.orm import Session
from dependecis import pegar_sessao, verificar_token
from schemas import PedidoSchemas, ItemPedidoSchema , ResponsePedidosSchema
from models import Pedido, Usuario, ItensPedido
from typing import List

roteador_ordens = APIRouter(prefix="/pedidos", tags=["pedidos"], dependencies=[Depends(verificar_token)])

@roteador_ordens.get("/")
async def pedidos():
    """
    Essa é a rota padrão do nosso sistema.
    """
    return {"mensagem":"Você acessou a rota de pedidos"}

@roteador_ordens.post("/pedido")
async def criar_pedido(pedido_schema:PedidoSchemas, session:Session = Depends(pegar_sessao)):
    novo_pedido = Pedido(usuario=pedido_schema.id_usuario)
    session.add(novo_pedido)
    session.commit()
    return{"mensagem":f"Pedido criado com sucesso. ID do pedido: {novo_pedido.id}"}

@roteador_ordens.post("/pedido/cancelar/{id_pedido}")
async def cancelar_pedido(id_pedido:int, session:Session = Depends(pegar_sessao),usuario:Usuario = Depends(verificar_token)):
    pedido = session.query(Pedido).filter(Pedido.id == id_pedido).first()
    if not pedido :
        raise HTTPException(status_code=400, detail="Pedido não encontrado")
    if not usuario.admin and usuario.id != pedido.usuario:
        raise HTTPException(status_code=400, detail="Você não tem autorização para fazer essa modificação")
    pedido.status = "CANCELADO"
    session.commit()
    return{
        "mensagem":f"Pedido número {id_pedido} cancelado com sucesso",
        "pedido":pedido
    }

@roteador_ordens.get("/listar")
async def listar_pedidos( session:Session = Depends(pegar_sessao),usuario:Usuario = Depends(verificar_token)):
    if usuario.admin == False:
        raise HTTPException(status_code=400, detail="Você não tem autorização para fazer essa operação")# tratamento de erro 
    else:
        pedidos = session.query(Pedido).all()# query verifica os dados no banco de dados e o all retorna todos os dados
        return{
            "pedidos": pedidos
        }

@roteador_ordens.post("/pedido/adicionar-item/{id_pedido}")
async def adicionar_item_pedido(id_pedido:int,item_pedido_schema:ItemPedidoSchema,session: Session = Depends(pegar_sessao),usuario: Usuario = Depends(verificar_token)):
    pedido = session.query(Pedido).filter(Pedido.id == id_pedido).first()
    if not pedido:
        raise HTTPException(status_code=400, detail="Pedido não existente")
    if not usuario.admin and usuario.id != pedido.usuario:
        raise HTTPException(status_code=401,detail="Você não tem permissão para fazer essa operação.")
    item_pedido = ItensPedido(item_pedido_schema.quantidade,item_pedido_schema.sabor,item_pedido_schema.tamanho,item_pedido_schema.preco_unitario,id_pedido)
    session.add(item_pedido)
    pedido.calcular_preco()
    session.commit()
    return{
        "mensagem":"Item criado com sucesso",
        "item_id":item_pedido.id,
        "preco_pedido":pedido.preco
    }

@roteador_ordens.post("/pedido/remover-item/{id_item_pedido}")
async def remover_item_pedido(id_item_pedido:int,
                              session: Session = Depends(pegar_sessao),
                              usuario: Usuario = Depends(verificar_token)):
    item_pedido = session.query(ItensPedido).filter(ItensPedido.id == id_item_pedido).first()
    pedido = session.query(Pedido).filter(Pedido.id==item_pedido.pedido).first()
    if not item_pedido:
        raise HTTPException(status_code=400, detail="Item no pedido não existente")
    if not usuario.admin and usuario.id != item_pedido.pedido.usuario:
        raise HTTPException(status_code=401,detail="Você não tem permissão para fazer essa operação.")
    session.delete(item_pedido)
    pedido.calcular_preco()
    session.commit()
    return{
        "mensagem":"Item removido com sucesso",
        "quantidade_itens_pedido":len(pedido.itens),
        "pedido":pedido
    }

@roteador_ordens.post("/pedido/finalizar/{id_pedido}")
async def finalizar_pedido(id_pedido:int, session:Session = Depends(pegar_sessao),usuario:Usuario = Depends(verificar_token)):
    pedido = session.query(Pedido).filter(Pedido.id == id_pedido).first()
    if not pedido :
        raise HTTPException(status_code=400, detail="Pedido não encontrado")
    if not usuario.admin and usuario.id != pedido.usuario:
        raise HTTPException(status_code=400, detail="Você não tem autorização para fazer essa modificação")
    pedido.status = "FINALIZADO"
    session.commit()
    return{
        "mensagem":f"Pedido número {id_pedido} finalizado com sucesso",
        "pedido":pedido
    }

@roteador_ordens.get("/pedido/{id_pedido}", response_model=ResponsePedidosSchema)
async def vizualizar_pedido(id_pedido:int, session:Session = Depends(pegar_sessao), usuario:Usuario = Depends(verificar_token)):
    pedido = session.query(Pedido).filter(Pedido.id == id_pedido).first()
    if not pedido:
        raise HTTPException(status_code=400,detail="Pedido não encontrado")
    if not usuario.admin and usuario.id != pedido.usuario:
        raise HTTPException(status_code=401, detail="Você não tem autorização para fazer essa modificação.")
    #return{
    #    "quantidade_item_pedido":len(pedido.itens),
    #    "pedido":pedido
    #}
    return pedido



@roteador_ordens.get("/listar/pedidos-usuario",response_model=List[ResponsePedidosSchema])
async def listar_pedidos(session:Session = Depends(pegar_sessao), usuario:Usuario = Depends(verificar_token)):
        pedidos = session.query(Pedido).filter(Pedido.usuario==usuario.id).all()
        return pedidos