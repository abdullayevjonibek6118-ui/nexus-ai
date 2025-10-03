import { apiGet, apiPost } from '@/lib/api'
import { revalidatePath } from 'next/cache'

async function createVac(formData: FormData) {
  'use server'
  const title = formData.get('title') as string
  const description = formData.get('description') as string
  const owner_id = Number(formData.get('owner_id')) || 1
  await apiPost('/vacancies/', { title, description, status: 'open', owner_id })
  revalidatePath('/vacancies')
}

export default async function VacanciesPage() {
  const vacancies = await apiGet<any[]>('/vacancies/')
  return (
    <main className="max-w-2xl mx-auto p-6 space-y-6">
      <h1 className="text-2xl font-semibold">Vacancies</h1>
      <ul className="space-y-2">
        {vacancies.map(v => (
          <li key={v.id} className="border rounded p-3">
            <div className="font-medium">{v.title}</div>
            <div className="text-sm text-gray-600">{v.description}</div>
          </li>
        ))}
      </ul>

      <form action={createVac} className="space-y-3 border rounded p-4">
        <input name="title" placeholder="Title" className="border p-2 w-full" required />
        <textarea name="description" placeholder="Description" className="border p-2 w-full" />
        <input name="owner_id" placeholder="Owner ID" className="border p-2 w-full" defaultValue="1" />
        <button type="submit" className="bg-black text-white px-4 py-2 rounded">Create</button>
      </form>
    </main>
  )
}


