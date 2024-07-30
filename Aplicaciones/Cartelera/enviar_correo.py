from django.core.mail import send_mail

def enviar_correo_nuevo_cine(nombre_cine, direccion_cine, telefono_cine):
    asunto = '¡Nuevo cine registrado!'
    mensaje = f"""
        Se ha registrado un nuevo cine en el sistema:

        Nombre: {nombre_cine}
        Dirección: {direccion_cine}
        Teléfono: {telefono_cine}

        ¡Saludos!
    """
    correo_electronico = 'llumiugsimichael@gmail.com'  # Reemplaza con tu correo electrónico
    send_mail(
        asunto,
        mensaje,
        correo_electronico,
        ['changoluisasteven02@gmail.com','michael.llumiugsi8127@utc.edu.ec','lenin.flores8004@utc.edu.ec']  # Agrega los correos electrónicos de destino
    )
