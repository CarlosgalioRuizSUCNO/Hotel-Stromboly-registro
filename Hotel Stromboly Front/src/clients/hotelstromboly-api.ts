export interface EvaluacionResponse {
  status: string;
  mensaje: string;
  data: {
    califica: boolean,
    habitacion: string | null,
  };
}
 
export async function evaluarCliente(edad: number, ingreso: number, n_personas: number): Promise<EvaluacionResponse> {
  const res = await fetch(`http://localhost:8000/evaluaciones/cliente?edad=${edad}&ingreso=${ingreso}&n_personas=${n_personas}`);

  if (!res.ok) {
    throw new Error("Un error sucedió en el sistema.")
  }
 
  return await res.json();
}