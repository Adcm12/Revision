import datetime
import pyttsx3

# Obtiene la hora actual
hora_actual = datetime.datetime.now().time()

# Convierte la hora actual en palabras
def hora_en_palabras(hora):
    horas = ["medianoche", "una", "dos", "tres", "cuatro", "cinco", "seis", "siete", "ocho", "nueve", "diez", "once", "doce"]
    minutos = ["", "un minuto", "dos minutos", "tres minutos", "cuatro minutos", "cinco minutos", "seis minutos", "siete minutos", "ocho minutos", "nueve minutos", "diez minutos", "once minutos", "doce minutos", "trece minutos", "catorce minutos", "quince minutos", "dieciséis minutos", "diecisiete minutos", "dieciocho minutos", "diecinueve minutos", "veinte minutos", "veintiún minutos", "veintidós minutos", "veintitrés minutos", "veinticuatro minutos", "veinticinco minutos", "veintiséis minutos", "veintisiete minutos", "veintiocho minutos", "veintinueve minutos", "treinta minutos", "treinta y un minutos", "treinta y dos minutos", "treinta y tres minutos", "treinta y cuatro minutos", "treinta y cinco minutos", "treinta y seis minutos", "treinta y siete minutos", "treinta y ocho minutos", "treinta y nueve minutos", "cuarenta minutos", "cuarenta y un minutos", "cuarenta y dos minutos", "cuarenta y tres minutos", "cuarenta y cuatro minutos", "cuarenta y cinco minutos", "cuarenta y seis minutos", "cuarenta y siete minutos", "cuarenta y ocho minutos", "cuarenta y nueve minutos"]

    if hora.minute == 0:
        return f"Son las {horas[hora.hour]} en punto."
    elif hora.minute == 15:
        return f"Son las {horas[hora.hour]} y cuarto."
    elif hora.minute == 30:
        return f"Son las {horas[hora.hour]} y media."
    elif hora.minute == 45:
        return f"Son las {horas[(hora.hour + 1) % 12]} menos cuarto."
    elif hora.minute < 30:
        return f"Son las {horas[hora.hour]} y {minutos[hora.minute]}."
    else:
        return f"Son las {horas[(hora.hour + 1) % 12]} menos {minutos[60 - hora.minute]}."

# Imprime la hora actual
print("Hora actual:", hora_actual.strftime("%H:%M"))

# Imprime la hora en palabras
hora_palabras = hora_en_palabras(hora_actual)
print(hora_palabras)

# Convierte la hora en palabras a voz
engine = pyttsx3.init()
engine.say(hora_palabras)
engine.runAndWait()
