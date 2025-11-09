@echo off
title Instalador - Creador de Mods Payday 2
color 0B
echo ================================
echo   CONFIGURANDO CREACION DE MODS
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
python -m pip install --upgrade pydub

echo.
echo Verificando FFmpeg...
ffmpeg -version >nul 2>&1
if errorlevel 1 (
    echo ⚠️ FFmpeg no está instalado.
    echo.
    echo Puedes instalarlo ejecutando (en PowerShell como Administrador):
    echo     choco install ffmpeg
    echo.
) else (
    echo ✅ FFmpeg detectado correctamente.
)

echo.
echo ✅ Instalación completa.
pause
