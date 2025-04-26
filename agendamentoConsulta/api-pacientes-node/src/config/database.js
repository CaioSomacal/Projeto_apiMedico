const { Sequelize } = require('sequelize');

// Criando a conexão com o banco de dados MySQL
const sequelize = new Sequelize('atendimento_db', 'root', '', {
  host: 'localhost',
  port: 3307,
  dialect: 'mysql',
  logging: false,  // Desabilita logs de consultas SQL
});

module.exports = sequelize;
