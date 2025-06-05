import { Bar } from 'react-chartjs-2'
import { Chart as ChartJS, BarElement, CategoryScale, LinearScale } from 'chart.js'

ChartJS.register(BarElement, CategoryScale, LinearScale)

const data = {
  labels: ['Jan', 'Feb', 'Mar', 'Apr', 'May'],
  datasets: [
    {
      label: 'Cost',
      data: [500, 800, 400, 900, 700],
      backgroundColor: 'rgba(99,102,241,0.5)',
    },
  ],
}

export default function Dashboard() {
  return (
    <section className="p-8">
      <h2 className="text-xl font-semibold mb-4">Sample Cost Trend</h2>
      <Bar data={data} />
    </section>
  )
}
