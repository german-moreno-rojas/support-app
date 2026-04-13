// src/app/page.tsx

'use client'

import { useState, useEffect } from "react"

export default function HomePage() {
  const [message, setMessage] = useState<string | null>(null);
  const [health, setHealth] = useState<string | null>(null);

  useEffect(() => {
    fetch(`${process.env.NEXT_PUBLIC_API_URL}/`)
      .then((res) => res.json())
      .then((data) => setMessage(data.message))
      .catch(() => setMessage("Error al conectar con el backend"))

    fetch(`${process.env.NEXT_PUBLIC_API_URL}/health`)
      .then((res) => res.json())
      .then((data) => setHealth(data.status))
      .catch(() => setHealth("Error en el healthcheck"))
  }, [])

  return (
    <main className="flex flex-col items-center justify-center min-h-screen p-8">
      <h1 className="text-3xl font-bold mb-4">
        Conexión del frontend con el backend😒😒
      </h1>

      <div className="space-y-3">
        <p>
          Estado de salud: <strong>{health || "Cargando..."}</strong>
        </p>
      </div>
    </main>
  )
}