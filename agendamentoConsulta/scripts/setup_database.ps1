# Requer MySQL instalado e no PATH
$MYSQL_PATH = "mysql.exe"
$DB_USER = "root"
$DB_PASSWORD = "sua_senha" # Altere para sua senha

Write-Host "Configurando banco de dados..."

# Executa scripts SQL
& $MYSQL_PATH -u $DB_USER -p$DB_PASSWORD -e "SOURCE scripts/database/init_db.sql"
& $MYSQL_PATH -u $DB_USER -p$DB_PASSWORD agendamento_consultas -e "SOURCE scripts/database/populate_test_data.sql"

Write-Host "Banco configurado com sucesso!"
Write-Host "Estrutura criada e dados de teste inseridos."