from app.pdf.pdf_reader import PDFReader
from app.pdf.motor_importacion import MotorImportacion

print("=" * 60)
print("JLR BANK PRO - PRUEBA DEL MOTOR DE IMPORTACIÓN")
print("=" * 60)

ruta = input("Ingrese la ruta completa del PDF: ")

# Mostrar el texto extraído del PDF
texto = PDFReader.extraer_texto(ruta)

print("\n")
print("=" * 80)
print("TEXTO EXTRAÍDO DEL PDF")
print("=" * 80)
print(texto[:5000])  # Muestra los primeros 5000 caracteres
print("=" * 80)

# Ejecutar el motor de importación
resultado = MotorImportacion.importar(ruta)

print("\n")
print("=" * 60)
print("RESULTADO DEL MOTOR")
print("=" * 60)
print("Banco detectado :", resultado["banco"])
print("Cantidad de movimientos :", len(resultado["movimientos"]))
print("=" * 60)

for movimiento in resultado["movimientos"]:
    print(movimiento)