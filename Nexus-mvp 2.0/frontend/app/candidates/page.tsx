import { apiGet, apiPost } from '@/lib/api'
import { revalidatePath } from 'next/cache'

async function createCandidate(formData: FormData) {
  'use server'
  const payload = {
    name: String(formData.get('name') || ''),
    email: String(formData.get('email') || ''),
    skills: String(formData.get('skills') || ''),
    experience: String(formData.get('experience') || ''),
    resume_url: String(formData.get('resume_url') || ''),
    vacancy_id: Number(formData.get('vacancy_id') || 1),
  }
  await apiPost('/candidates/', payload)
  revalidatePath('/candidates')
}

export default async function CandidatesPage() {
  const candidates = await apiGet<any[]>('/candidates/')
  return (
    <main className="max-w-2xl mx-auto p-6 space-y-6">
      <h1 className="text-2xl font-semibold">Candidates</h1>
      <ul className="space-y-2">
        {candidates.map(c => (
          <li key={c.id} className="border rounded p-3">
            <div className="font-medium">{c.name}</div>
            <div className="text-sm text-gray-600">{c.email}</div>
          </li>
        ))}
      </ul>

      <form action={createCandidate} className="space-y-3 border rounded p-4">
        <input name="name" placeholder="Name" className="border p-2 w-full" required />
        <input name="email" placeholder="Email" className="border p-2 w-full" />
        <input name="skills" placeholder="Skills" className="border p-2 w-full" />
        <input name="experience" placeholder="Experience" className="border p-2 w-full" />
        <input name="resume_url" placeholder="Resume URL" className="border p-2 w-full" />
        <input name="vacancy_id" placeholder="Vacancy ID" className="border p-2 w-full" defaultValue="1" />
        <button type="submit" className="bg-black text-white px-4 py-2 rounded">Create</button>
      </form>
    </main>
  )
}


