import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import { BrowserRouter,Routes, Route } from 'react-router-dom'
import HomePage from './pages/HomePage'
import TaskForm   from './pages/TaskForm'
import NavBar from './components/NavBar'
function App() {
  return (
      <BrowserRouter>
        <div className='container mx-auto px-10'>
          <NavBar />
        <Routes>
          <Route path="/" element={<HomePage/>}/>
          <Route path="/tasks/:id" element={<TaskForm/>}/>
          <Route path="/tasks/new" element={<TaskForm/>}/>

        </Routes>
        </div>
      </BrowserRouter>
    )
}

export default App
