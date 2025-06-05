import { Route, Routes } from 'react-router-dom'
import Header from './components/Header'
import Home from './pages/Home'
import Dashboard from './pages/Dashboard'

export default function App() {
  return (
    <div className="min-h-screen flex flex-col">
      <Header />
      <main className="flex-1 container mx-auto p-4">
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/dashboard" element={<Dashboard />} />
        </Routes>
      </main>
    </div>
  )
}
