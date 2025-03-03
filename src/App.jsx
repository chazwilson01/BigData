import { useState } from 'react'
import './App.css'
import ResourcesPage from './Page'
function App() {
  const [count, setCount] = useState(0)

  return (
    <>
      <ResourcesPage/>
    </>
  )
}

export default App
