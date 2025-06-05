import { Link } from 'react-router-dom'
import { useAppStore } from '../store/useAppStore'

export default function Header() {
  const toggle = useAppStore((s) => s.toggle)
  return (
    <header className="bg-gray-800 text-white p-4 flex justify-between">
      <h1 className="font-bold">IT Fin Portal</h1>
      <nav className="space-x-4 flex items-center">
        <Link className="hover:underline" to="/">Home</Link>
        <Link className="hover:underline" to="/dashboard">Dashboard</Link>
        <button onClick={toggle} className="ml-4 px-2 py-1 border rounded">
          Toggle Theme
        </button>
      </nav>
    </header>
  )
}
