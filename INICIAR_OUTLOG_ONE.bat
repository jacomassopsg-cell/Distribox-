@echo off
chcp 65001 >nul
title OUTLOG ONE - OPERACAO LOGISTICA INTEGRADA
cd /d "%~dp0"

echo =====================================================
echo             OUTLOG ONE - INICIALIZACAO
echo =====================================================
echo.
set "OUTLOG_PORT=8010"

where py >nul 2>nul
if errorlevel 1 (
  where python >nul 2>nul
  if errorlevel 1 (
    echo Python nao encontrado.
    echo Instale o Python 3.10 ou superior e marque Add Python to PATH.
    pause
    exit /b 1
  )
  set "PYTHON_CMD=python"
) else (
  set "PYTHON_CMD=py"
)

if not exist ".venv\Scripts\python.exe" (
  echo Preparando o sistema pela primeira vez...
  %PYTHON_CMD% -m venv .venv
  if errorlevel 1 goto :erro
)

echo Verificando componentes...
".venv\Scripts\python.exe" -m pip install -r requirements.txt
if errorlevel 1 goto :erro

echo.
echo OutLog One V3.1 disponivel em http://127.0.0.1:%OUTLOG_PORT%
start "" http://127.0.0.1:%OUTLOG_PORT%
".venv\Scripts\python.exe" -m uvicorn app:app --host 127.0.0.1 --port %OUTLOG_PORT%
goto :fim

:erro
echo.
echo Nao foi possivel concluir a inicializacao.
echo Confira a internet e a instalacao do Python e tente novamente.
:fim
pause

