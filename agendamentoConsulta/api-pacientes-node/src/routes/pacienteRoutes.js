const express = require('express');
const router = express.Router();
const pacienteController = require('../controllers/pacienteController');

// Rota para criar um paciente
router.post('/', pacienteController.criarPaciente);

// Rota para listar todos os pacientes
router.get('/', pacienteController.listarPacientes);

// Rota para buscar um paciente por ID
router.get('/:id', pacienteController.buscarPacientePorId);

// Rota para atualizar um paciente
router.put('/:id', pacienteController.atualizarPaciente);

// Rota para deletar um paciente
router.delete('/:id', pacienteController.deletarPaciente);

module.exports = router;
