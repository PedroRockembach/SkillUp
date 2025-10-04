import { useState } from 'react'

function App() {
  return (
    <>
      <header className='bg-blue-400 flex justify-between items-center h-[13vh] px-9'>
        <div className='flex items-center gap-4'>
          <img src="" alt="SkillUp logo" className='text-[1rem] font-[700] '/>
          <h2 className='text-[1rem] font-[700]'>Menu</h2>
        </div>
        <button className='flex bg-orange-400 px-[1rem] py-[0.8rem] rounded-[1rem] text-[1.2rem] font-[700]'><a href="">Cadastrar</a></button>
      </header>
      <main>
        <section className='flex flex-col gap-4 items-center justify-center h-[87vh]'>
          <h1 className='text-[1.5rem] font-[700]'>Bem-vindo ao SkillUp</h1>
          <h2 className='text-[1rem] font-[700]'>Aprenda novas habilidades e avance na sua carreira</h2>
          <div className='flex flex-col gap-2'>
            <input type="text" placeholder='Nome' className='border border-black rounded-[0.5rem] p-2'/>
            <input type="email" placeholder='Email' className='border border-black rounded-[0.5rem] p-2'/>
            <input type="password" placeholder='Senha' className='border border-black rounded-[0.5rem] p-2'/>
            <button className='bg-blue-400 px-[1rem] py-[0.8rem] rounded-[1rem] text-[1.2rem] font-[700]'>Cadastrar</button>
          </div>
        </section>
      </main>
    </>
  )
}

export default App
