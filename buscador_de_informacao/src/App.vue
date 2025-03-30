<template>
  <div>
    <h1>Realizando uma busca</h1>

    <!-- Botão de busca -->
    <button @click="buscarOperadores">Buscar Cadastro de Operadores</button>

    <!--Tabela para exibir os operadores -->
    <table >
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
        <tr v-for="operador in operadores" :key="operador.registro_ans">
          <td>{{ operador.registro_ans }}</td>
          <td>{{ operador.cnpj }}</td>
          <td>{{ operador.razao_socias }}</td>
          <td>{{ operador.nome_fantasia }}</td>
          <td>{{ operador.modalidade }}</td>
          <td>{{ operador.logradouro }}</td>
          <td>{{ operador.numero }}</td>
          <td>{{ operador.complemento }}</td>
          <td>{{ operador.bairro }}</td>
          <td>{{ operador.cidade }}</td>
          <td>{{ operador.uf }}</td>
          <td>{{ operador.cep }}</td>
          <td>{{ operador.ddd }}</td>
          <td>{{ operador.telefone }}</td>
          <td>{{ operador.fax }}</td>
          <td>{{ operador.endereco_eletronico }}</td>
          <td>{{ operador.representante }}</td>
          <td>{{ operador.cargo_representante }}</td>
          <td>{{ operador.regiao_de_comercializacao }}</td>
          <td>{{ operador.data_registro_ans }}</td>
        </tr>
      </tbody>
    </table>
    <!-- Caso não haja operadores cadastrados -->
    <p>No records found</p>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      operadores: []  // Armazenará os dados dos operadores
    };
  },
  methods: {
    // Método que será chamado ao clicar no botão
    buscarOperadores() {
      axios.get('http://localhost:5000/api/operadores')  // Requisição ao servidor
        .then(response => {
          this.operadores = response.data;  // Atualiza a lista de operadores com os dados retornados
        })
        .catch(error => {
          console.error("Erro ao buscar operadores:", error);
        });
    }
  }
};
</script>

<style scoped>
/* Estilos para a tabela */
table {
  width: 100%;
  border-collapse: collapse;
  margin-top: 20px;
}

th, td {
  padding: 8px;
  text-align: left;
  border: 1px solid #ddd;
}



button {
  padding: 10px 15px;
  font-size: 16px;
  margin-bottom: 20px;
  cursor: pointer;
  background-color: #4CAF50;
  color: white;
  border: none;
  border-radius: 4px;
}

button:hover {
  background-color: #45a049;
}
</style>