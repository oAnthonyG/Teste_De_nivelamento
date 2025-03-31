<template>
  <div>
    <h1>Lista de cadastros de operadoras com os registros mais relevantes</h1>
    <table>
    <thead>
        <tr>
          <th>Registro_ANS</th>
          <th>CNPJ</th>
          <th>Razão_Social</th>
          <th>Nome_Fantasia</th>
          <th>Modalidade</th>
          <th>Logradouro</th>
          <th>Numero</th>
          <th>Complemento</th>
          <th>Bairro</th>
          <th>Cidade</th>
          <th>UF</th>
          <th>CEP</th>
          <th>DDD</th>
          <th>Telefone</th>
          <th>Fax</th>
          <th>Endereco_eletronico</th>
          <th>Representante</th>
          <th>Cargo_Representante</th>
          <th>Regiao_de_Comercializacao</th>
          <th>Data_Registro_ANS</th>
        </tr>
      </thead>

  <tbody>
    <tr v-for="relatorio of relatorios" :key="relatorio.Registro_ANS">
        <td>{{ relatorio.Registro_ANS }}</td>
        <td>{{ relatorio.CNPJ }}</td>
          <td>{{ relatorio.Razao_Social }}</td>
          <td> {{ relatorio.Nome_Fantasia }}</td>
          <td>{{ relatorio.Modalidade }}</td>
          <td>{{ relatorio.Logradouro }}</td>
          <td>{{ relatorio.Numero }}</td>
          <td>{{ relatorio.Complemento }}</td>
          <td>{{ relatorio.Bairro }}</td>
          <td>{{ relatorio.Cidade }}</td>
          <td>{{ relatorio.UF }}</td>
          <td>{{ relatorio.CEP }}</td>
          <td>{{ relatorio.DDD }}</td>
          <td>{{ relatorio.Telefone }}</td>
          <td>{{ relatorio.Fax }}</td>
          <td>{{ relatorio.Endereco_eletronico }}</td>
          <td>{{ relatorio.Representante }}</td>
          <td>{{ relatorio.Cargo_Representante }}</td>
          <td>{{ relatorio.Regiao_de_Comercializacao }}</td>
          <td>{{ relatorio.Data_Registro_ANS }}</td>

    </tr>
  </tbody>
  </table>
  </div>
</template>

<script>
import Relatorio from './services/relatorios'

export default {
  data(){
    return {
      relatorios: []
    }
  },
  mounted(){
    Relatorio.listar().then(resposta =>{
      this.relatorios = resposta.data
    })
  }
}
</script>

<style scoped>
table {
  text-align: center;
  border-collapse: collapse;
}

th {
  background-color: #4CAF50;
  color: white;
  padding: 12px;
  font-size: 12px;
  border: 1px solid white;
}

td {
  padding: 10px;
  border: 1px solid #ddd;
  font-size: 10px;
}
</style>