const express = require('express');
const bodyParser = require('body-parser');
const { sequelize } = require('./models/Paciente');
const pacienteRoutes = require('./routes/pacienteRoutes');

const app = express();
const port = 3000;

// Middlewares
app.use(bodyParser.json());

// Rotas
app.use('/api/pacientes', pacienteRoutes);

// Iniciar o servidor e sincronizar com o banco de dados
sequelize.sync({ force: false }).then(() => {
  app.listen(port, () => {
    console.log(`Servidor rodando na porta ${port} 🚀`);
  });
});
