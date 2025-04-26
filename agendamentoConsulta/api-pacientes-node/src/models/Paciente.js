const { DataTypes } = require('sequelize');
const sequelize = require('../config/database');

// Definindo o modelo de Paciente
const Paciente = sequelize.define('Paciente', {
  nome: {
    type: DataTypes.STRING,
    allowNull: false,
  },
  idade: {
    type: DataTypes.INTEGER,
    allowNull: false,
  },
  endereco: {
    type: DataTypes.STRING,
    allowNull: false,
  },
}, {});

module.exports = { sequelize, Paciente };
