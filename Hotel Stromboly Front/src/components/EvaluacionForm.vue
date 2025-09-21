<script setup lang="ts">
import { ref } from 'vue'
import { type EvaluacionResponse, evaluarCliente } from '../clients/hotelstromboly-api';
 
const edad = ref<number>(0);
const ingreso = ref<number>(0);
const n_personas = ref<number>(0);
const metodo_pago = ref<string>('efectivo');
const n_dni = ref<number>(12345672);
const resultado = ref<EvaluacionResponse | null>(null);
 
async function onSubmit() {
  try {
    resultado.value = await evaluarCliente(edad.value, ingreso.value, n_personas.value, metodo_pago.value, n_dni.value);
  } catch(e) {
    window.alert('Ocurrió un error al procesar la solicitud, intente nuevamente');
  }
}
</script>
 
<template>
  <h1 style="font-family: 'Bitcount Grid Double'" >Financiera Oh</h1>
  <p style="font-family: 'Bitcount Grid Double'; font-size: 20px;">Bienvenido, coloque sus datos para conocer si puede alquilar una de nuestras habitaciones.</p>
  <form @submit.prevent="onSubmit">
    <label style="font-family: 'Bitcount Grid Double'" class="mx-2" >Edad:</label>
    <input type="number" v-model="edad" />

    <label style="font-family: 'Bitcount Grid Double'" class="mx-2" >Ingresos:</label>
    <input type="number" v-model="ingreso"/>

    <label style="font-family: 'Bitcount Grid Double'" class="mx-2" >Numero de personas:</label>
    <input type="number" v-model="n_personas"/>

    <br>

    <label style="font-family: 'Bitcount Grid Double'" class="mx-2" >Documento de identidad:</label>
    <input type="number" v-model="n_dni"/>

    <label style="font-family: 'Bitcount Grid Double'" class="mx-2" >Metodo de pago:</label>
    <select v-model="metodo_pago">
      <option value="efectivo">Efectivo</option>
      <option value="tarjeta">Tarjeta</option>
      <option value="transferencia">Transferencia</option>
    </select>

    <button style="font-family: 'Bitcount Grid Double'" class="mx-2" type="submit">Evaluar</button>
  </form>
  <div v-if="resultado">
    <h3 style="font-family: 'Bitcount Grid Double'" > {{ resultado.status }} </h3>
    <h3 style="font-family: 'Bitcount Grid Double'" > {{ resultado.mensaje }} </h3>
    <p style="font-family: 'Bitcount Grid Double'" > Tipo de habitacion: {{ resultado.data.habitacion }}</p>
  </div>
</template>
 
<style scoped>
</style>
