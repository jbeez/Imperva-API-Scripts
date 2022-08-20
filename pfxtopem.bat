@echo off
set RANDFILE=%~dp0\.rnd
set /p KeyPass=Enter Key Password:
cls

openssl pkcs12 -in %~nx1 -passin pass:"%KeyPass%" -passout pass:"%KeyPass%" -nocerts -out %~n1.key
openssl pkcs12 -in %~nx1 -passin pass:"%KeyPass%" -clcerts -nokeys -out tempcert.crt
openssl pkcs12 -in %~nx1 -passin pass:"%KeyPass%" -cacerts -nokeys -out tempcacert.crt

type tempcert.crt tempcacert.crt > %~n1.pem
cls
del tempcert.crt tempcacert.crt
echo.
echo Created %~n1.key and %~n1.pem from %~nx1
echo.
pause
