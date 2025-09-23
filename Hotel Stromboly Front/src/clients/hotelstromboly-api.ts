export interface EvaluacionResponse {
  status: string;
  mensaje: string;
  data: {
    califica: boolean,
    habitacion: string | null,
    descripcion: string | null
  };
}
 
export async function evaluarCliente(edad: number, ingreso: number, n_personas: number, metodo_pago: string, n_dni: number): Promise<EvaluacionResponse> {
  const res = await fetch(`http://localhost:8000/evaluaciones/cliente?edad=${edad}&ingreso=${ingreso}&n_personas=${n_personas}&metodo_pago=${metodo_pago}&n_dni=${n_dni}`);

  if (!res.ok) {
    throw new Error("Un error sucedió en el sistema.")
  }
 
  return await res.json();
}