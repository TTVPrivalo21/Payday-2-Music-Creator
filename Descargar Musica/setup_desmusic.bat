@echo off
title Instalador - Descargador de Musica
color 0B
echo ================================
echo   CONFIGURANDO DESCARGADOR DE MUSICA
echo ================================
echo.

echo Verificando Python...
python --version >nul 2>&1
if errorlevel 1 (
    echo ⚠️ Python no está instalado o no está en PATH.
    echo Por favor instala Python 3.10 o superior desde https://www.python.org/downloads/
    pause
    exit /b
)

echo Instalando dependencias necesarias...
python -m pip install --upgrade pip
python -m pip install --upgrade yt-dlp

echo.
echo ✅ Instalación completa.
pause
