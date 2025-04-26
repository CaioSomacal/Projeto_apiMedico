const { Paciente } = require('../models/Paciente.js');

// Criar um novo paciente
const criarPaciente = async (req, res) => {
  try {
    const { nome, idade, endereco } = req.body;
    const paciente = await Paciente.create({ nome, idade, endereco });
    res.status(201).json(paciente);
  } catch (error) {
    res.status(500).json({ error: 'Erro ao criar paciente' });
  }
};

// Buscar todos os pacientes
const listarPacientes = async (req, res) => {
  try {
    const pacientes = await Paciente.findAll();
    console.log("Esta entrando aqui")
    res.status(200).json(pacientes);
  } catch (error) {
    res.status(500).json({ error: 'Erro ao listar pacientes' });
  }
};

// Buscar um paciente por ID
const buscarPacientePorId = async (req, res) => {
  try { 
    let { id } = req.params;
    id = parseInt(id, 10);
    console.log(id)
    const paciente = await Paciente.findByPk(id);
    if (!paciente) {
      return res.status(404).json({ error: 'Paciente não encontrado' });
    }
    res.status(200).json(paciente);
  } catch (error) {
    res.status(500).json({ error: 'Erro ao buscar paciente' });
  }
};

// Atualizar um paciente
const atualizarPaciente = async (req, res) => {
  try {
    const { id } = req.params;
    const { nome, idade, endereco } = req.body;

    const paciente = await Paciente.findByPk(id);
    if (!paciente) {
      return res.status(404).json({ error: 'Paciente não encontrado' });
    }

    paciente.nome = nome;
    paciente.idade = idade;
    paciente.endereco = endereco;
    await paciente.save();

    res.status(200).json(paciente);
  } catch (error) {
    res.status(500).json({ error: 'Erro ao atualizar paciente' });
  }
};

// Deletar um paciente
const deletarPaciente = async (req, res) => {
  try {
    const { id } = req.params;
    const paciente = await Paciente.findByPk(id);
    if (!paciente) {
      return res.status(404).json({ error: 'Paciente não encontrado' });
    }

    await paciente.destroy();
    res.status(204).send();
  } catch (error) {
    res.status(500).json({ error: 'Erro ao deletar paciente' });
  }
};

module.exports = {
  criarPaciente,
  listarPacientes,
  buscarPacientePorId,
  atualizarPaciente,
  deletarPaciente,
};
