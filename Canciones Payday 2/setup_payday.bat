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
    echo ⚠️ Python no esta instalado o no esta en PATH.
    echo Por favor instala Python desde https://www.python.org/downloads/
    pause
    exit /b
)

echo Instalando dependencias de Python...
python -m pip install --upgrade pip
python -m pip install --upgrade pydub yt-dlp

echo.
echo Verificando FFmpeg...
ffmpeg -version >nul 2>&1
if errorlevel 1 (
    echo ⚠️ FFmpeg no detectado. Instalando automaticamente con winget...
    winget install ffmpeg --accept-source-agreements --accept-package-agreements
    echo.
    echo ================================================================
    echo ⚠️ ATENCION: Como FFmpeg se acaba de instalar, necesitas
    echo CERRAR ESTA VENTANA y cualquier otro editor (como VS Code)
    echo antes de ejecutar tus scripts de Python.
    echo ================================================================
) else (
    echo ✅ FFmpeg detectado correctamente en el sistema.
)

echo.
echo ✅ Instalacion completa.
pause