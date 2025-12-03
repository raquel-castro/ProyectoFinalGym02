from datetime import date
from src.gimnasio_app.services.gestion_socios import GestionSocios
from src.gimnasio_app.services.gestion_membresias import GestionMembresias
from src.gimnasio_app.services.gestion_clases import GestionClases
from src.gimnasio_app.services.gestion_asistencias import GestionAsistencias
from src.gimnasio_app.services.reportes import GeneradorReportes
from src.gimnasio_app.models.instructor import Instructor
from src.gimnasio_app.utils.validadores import Validadores
from src.gimnasio_app.utils.formatters import Formateadores


def pausar():
    input("\nPresione ENTER para continuar...")


def menu_principal():
    socios_srv = GestionSocios()
    membresias_srv = GestionMembresias()
    clases_srv = GestionClases()
    asistencias_srv = GestionAsistencias()
    reportes_srv = GeneradorReportes(socios_srv.repo, asistencias_srv.repo, clases_srv.repo, membresias_srv)

    instructores = [
        Instructor(1, "Ana Torres", "Spinning"),
        Instructor(2, "Luis Díaz", "Zumba"),
        Instructor(3, "María Gómez", "Yoga"),
        Instructor(4, "Carlos Ruiz", "Pilates"),
        Instructor(5, "Pedro López", "Boxeo"),
        Instructor(6, "Laura Sánchez", "Baile"),
    ]
    for inst in instructores:
        clases_srv.registrar_tipo_clase(inst.especialidad)

    while True:
        print("\n" + "=" * 45)
        print("      SISTEMA DE GESTIÓN DE GIMNASIO")
        print("=" * 45)
        print("1. Gestión de miembros")
        print("2. Gestión de membresías")
        print("3. Registro de asistencias")
        print("4. Gestión de clases")
        print("5. Reportes")
        print("6. Salir")
        print("=" * 45)
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            menu_miembros(socios_srv)
        elif opcion == "2":
            menu_membresias(socios_srv, membresias_srv)
        elif opcion == "3":
            menu_asistencias(socios_srv, asistencias_srv)
        elif opcion == "4":
            menu_clases(socios_srv, clases_srv, instructores)
        elif opcion == "5":
            menu_reportes(reportes_srv)
        elif opcion == "6":
            print("Saliendo del sistema. ¡Hasta luego!")
            break
        else:
            print("Opción inválida.")
            pausar()


def menu_reportes(reportes_srv: GeneradorReportes):
    while True:
        print("\n------------ REPORTES DEL GIMNASIO -----------")
        print("1. Resumen de actividad (hoy)")
        print("2. Resumen de actividad (otra fecha)")
        print("3. Total de socios")
        print("4. Socios activos vs inactivos")
        print("5. Volver al menú principal")
        print("----------------------------------------------")
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            resumen = reportes_srv.reporte_resumen()
            print("\n" + "=" * 50)
            print("RESUMEN DE ACTIVIDAD - HOY")
            print("=" * 50)
            for clave, valor in resumen.items():
                print(f"{clave.replace('_', ' ').title()}: {valor}")
            print("=" * 50)
            pausar()

        elif opcion == "2":
            fecha_str = input("Fecha (YYYY-MM-DD): ").strip()
            try:
                anio, mes, dia = [int(x) for x in fecha_str.split("-")]
                fecha_consulta = date(anio, mes, dia)
                resumen = reportes_srv.reporte_resumen(fecha_consulta)
                print("\n" + "=" * 50)
                print(f"RESUMEN DE ACTIVIDAD - {fecha_consulta}")
                print("=" * 50)
                for clave, valor in resumen.items():
                    print(f"{clave.replace('_', ' ').title()}: {valor}")
                print("=" * 50)
            except Exception as e:
                print(f"Error al procesar la fecha: {e}")
            pausar()

        elif opcion == "3":
            total = reportes_srv.total_socios()
            print(f"\nTotal de socios registrados: {total}")
            pausar()

        elif opcion == "4":
            activos = reportes_srv.total_socios_activos()
            inactivos = reportes_srv.total_socios_inactivos()
            total = activos + inactivos
            print("\n" + "=" * 50)
            print("ESTADO DE SOCIOS")
            print("=" * 50)
            print(f"Total de socios: {total}")
            print(f"Socios activos: {activos}")
            print(f"Socios inactivos: {inactivos}")
            if total > 0:
                porcentaje_activos = (activos / total) * 100
                print(f"Porcentaje activo: {porcentaje_activos:.1f}%")
            print("=" * 50)
            pausar()

        elif opcion == "5":
            break
        else:
            print("Opción inválida.")
            pausar()


def menu_miembros(socios_srv: GestionSocios):
    while True:
        print("\n------------- GESTIÓN DE MIEMBROS -------------")
        print("1. Registrar nuevo miembro")
        print("2. Editar datos de miembro")
        print("3. Buscar miembro por DNI")
        print("4. Listar miembros activos")
        print("5. Activar / desactivar miembro")
        print("6. Volver al menú principal")
        print("----------------------------------------------")
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            # Validar cada campo antes de intentar registrar; no se avanza hasta que sea válido
            while True:
                dni = input("Documento de identidad (DNI): ").strip()
                try:
                    Validadores.validar_dni(dni)
                    break
                except Exception as e:
                    print(f"DNI inválido: {e}")

            while True:
                nombres = input("Nombres: ").strip()
                try:
                    Validadores.validar_nombre(nombres)
                    break
                except Exception as e:
                    print(f"Nombres inválidos: {e}")

            while True:
                apellidos = input("Apellidos: ").strip()
                try:
                    Validadores.validar_apellido(apellidos)
                    break
                except Exception as e:
                    print(f"Apellidos inválidos: {e}")

            while True:
                telefono = input("Teléfono: ").strip()
                try:
                    Validadores.validar_telefono(telefono)
                    break
                except Exception as e:
                    print(f"Teléfono inválido: {e}")

            while True:
                correo = input("Correo: ").strip()
                try:
                    Validadores.validar_correo(correo)
                    break
                except Exception as e:
                    print(f"Correo inválido: {e}")

            try:
                socio = socios_srv.registrar(dni, nombres, apellidos, telefono, correo)
                print(f"Miembro registrado correctamente con código: {socio.dni}")
            except Exception as e:
                # esto captura errores inesperados provenientes del servicio/repo
                print(f"Error al registrar miembro: {e}")
            pausar()

        elif opcion == "2":
            dni = input("DNI del miembro a editar: ").strip()
            socio = socios_srv.buscar_por_dni(dni)
            if not socio:
                print("Miembro no encontrado.")
                pausar()
                continue
            print(f"Editando a: {socio}")
            nuevos_nombres = input("Nuevos nombres (ENTER para mantener): ").strip()
            nuevos_apellidos = input("Nuevos apellidos (ENTER para mantener): ").strip()
            nuevo_telefono = input("Nuevo teléfono (ENTER para mantener): ").strip()
            nuevo_correo = input("Nuevo correo (ENTER para mantener): ").strip()
            try:
                socios_srv.editar(
                    dni,
                    nombres=nuevos_nombres or None,
                    apellidos=nuevos_apellidos or None,
                    telefono=nuevo_telefono or None,
                    correo=nuevo_correo or None,
                )
                print("Datos actualizados correctamente.")
            except Exception as e:
                print(f"Error al editar: {e}")
            pausar()

        elif opcion == "3":
            dni = input("DNI del miembro: ").strip()
            socio = socios_srv.buscar_por_dni(dni)
            if socio:
                print(socio)
            else:
                print("Miembro no encontrado.")
            pausar()

        elif opcion == "4":
            activos = socios_srv.listar_activos()
            if not activos:
                print("No hay miembros activos.")
            else:
                print("\nMiembros activos:")
                listado_formateado = Formateadores.formatear_lista_simples([str(s) for s in activos])
                print(listado_formateado)
            pausar()

        elif opcion == "5":
            dni = input("DNI del miembro: ").strip()
            socio = socios_srv.buscar_por_dni(dni)
            if not socio:
                print("Miembro no encontrado.")
                pausar()
                continue
            print(f"Estado actual: {'Activo' if socio.estado_activo else 'Inactivo'}")
            print("1. Activar")
            print("2. Desactivar")
            eleccion = input("Seleccione: ").strip()
            if eleccion == "1":
                socios_srv.activar(dni)
                print("Miembro activado.")
            elif eleccion == "2":
                socios_srv.desactivar(dni)
                print("Miembro desactivado.")
            else:
                print("Opción inválida.")
            pausar()

        elif opcion == "6":
            break
        else:
            print("Opción inválida.")
            pausar()


def menu_membresias(socios_srv: GestionSocios, membresias_srv: GestionMembresias):
    while True:
        print("\n----------- GESTIÓN DE MEMBRESÍAS -----------")
        print("1. Asignar membresía a miembro")
        print("2. Renovar membresía de miembro")
        print("3. Ver estado de membresía de un miembro")
        print("4. Volver al menú principal")
        print("--------------------------------------------")
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            dni = input("DNI del miembro: ").strip()
            socio = socios_srv.buscar_por_dni(dni)
            if not socio:
                print("Miembro no encontrado.")
                pausar()
                continue

            print("Tipos de membresía:")
            print("1) 90 días")
            print("2) 180 días")
            print("3) 365 días")
            tipo = input("Seleccione tipo: ").strip()

            if tipo == "1":
                dias = 90
            elif tipo == "2":
                dias = 180
            elif tipo == "3":
                dias = 365
            else:
                print("Opción inválida.")
                pausar()
                continue

            membresia = membresias_srv.crear(f"{dias} días", dias)
            socios_srv.asignar_membresia(dni, membresia)
            print(f"Membresía de {dias} días asignada a {socio.nombres} {socio.apellidos}.")
            print(f"Inicio: {membresia.fecha_inicio} - Fin: {membresia.fecha_fin}")
            pausar()

        elif opcion == "2":
            dni = input("DNI del miembro: ").strip()
            socio = socios_srv.buscar_por_dni(dni)
            if not socio or not socio.membresia:
                print("El miembro no tiene membresía asignada.")
                pausar()
                continue
            membresias_srv.renovar(socio.membresia)
            print("Membresía renovada.")
            print(f"Nueva vigencia: {socio.membresia.fecha_inicio} - {socio.membresia.fecha_fin}")
            pausar()

        elif opcion == "3":
            dni = input("DNI del miembro: ").strip()
            socio = socios_srv.buscar_por_dni(dni)
            if not socio or not socio.membresia:
                print("Miembro sin membresía.")
            else:
                m = socio.membresia
                estado = "Activa" if m.esta_activa() else "Vencida"
                print(f"Membresía: {m.tipo} - {estado}")
                print(f"Inicio: {m.fecha_inicio} - Fin: {m.fecha_fin}")
            pausar()

        elif opcion == "4":
            break
        else:
            print("Opción inválida.")
            pausar()


def menu_asistencias(socios_srv: GestionSocios, asistencias_srv: GestionAsistencias):
    while True:
        print("\n----------- REGISTRO DE ASISTENCIAS -----------")
        print("1. Registrar asistencia (por DNI)")
        print("2. Ver historial de asistencia de un miembro")
        print("3. Ver asistencias del día")
        print("4. Volver al menú principal")
        print("----------------------------------------------")
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            while True:
                dni = input("DNI del miembro: ").strip()
                try:
                    Validadores.validar_dni(dni)
                    break
                except Exception as e:
                    print(f"DNI inválido: {e}")

            socio = socios_srv.buscar_por_dni(dni)
            if not socio:
                print("Miembro no encontrado.")
            else:
                asistencia = asistencias_srv.registrar_asistencia(socio)
                print(
                    f"Asistencia registrada para {socio.nombres} {socio.apellidos} "
                    f"a las {asistencia.hora} - {asistencia.fecha}"
                )
            pausar()

        elif opcion == "2":
            while True:
                dni = input("DNI del miembro: ").strip()
                try:
                    Validadores.validar_dni(dni)
                    break
                except Exception as e:
                    print(f"DNI inválido: {e}")

            socio = socios_srv.buscar_por_dni(dni)
            if not socio:
                print("Miembro no encontrado.")
                pausar()
                continue
            historial = asistencias_srv.historial_por_socio(socio)
            if not historial:
                print("El miembro no tiene asistencias registradas.")
            else:
                print(f"Historial de {socio.nombres} {socio.apellidos}:")
                lineas = [f"{a.fecha} {a.hora}" for a in historial]
                listado = Formateadores.formatear_lista_simples(lineas)
                print(listado)
            pausar()

        elif opcion == "3":
            hoy = date.today()
            asistencias_hoy = asistencias_srv.asistencias_del_dia(hoy)
            if not asistencias_hoy:
                print("No hay asistencias registradas para hoy.")
            else:
                print(f"Asistencias del día {hoy}:")
                lineas = [f"{a.socio.nombres} {a.socio.apellidos} a las {a.hora}" for a in asistencias_hoy]
                listado = Formateadores.formatear_lista_simples(lineas)
                print(listado)
            pausar()

        elif opcion == "4":
            break
        else:
            print("Opción inválida.")
            pausar()


def menu_clases(socios_srv: GestionSocios, clases_srv: GestionClases, instructores):
    while True:
        print("\n-------------- GESTIÓN DE CLASES --------------")
        print("1. Crear clase")
        print("2. Listar clases del día")
        print("3. Inscribir miembro a clase")
        print("4. Ver inscritos en una clase")
        print("5. Volver al menú principal")
        print("----------------------------------------------")
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            tipos = clases_srv.obtener_tipos_clase()
            print("Tipos de clase disponibles:")
            for idx, t in enumerate(tipos, start=1):
                print(f"{idx}) {t}")
            tipo_idx = input("Seleccione tipo: ").strip()
            try:
                tipo_idx = int(tipo_idx)
                tipo = tipos[tipo_idx - 1]
            except (ValueError, IndexError):
                print("Opción inválida.")
                pausar()
                continue

            fecha_str = input("Fecha (YYYY-MM-DD): ").strip()
            hora_str = input("Hora (HH:MM): ").strip()
            cupo_str = input("Cupo máximo: ").strip()
            try:
                cupo = int(cupo_str)
                anio, mes, dia = [int(x) for x in fecha_str.split("-")]
                fecha = date(anio, mes, dia)
            except Exception:
                print("Datos de fecha u hora/cupo inválidos.")
                pausar()
                continue

            instructor = next((i for i in instructores if i.especialidad.lower() == tipo.lower()), None)
            if not instructor:
                instructor = Instructor(999, "Instructor Genérico", tipo)

            clase = clases_srv.crear(tipo, instructor, cupo, fecha, hora_str)
            print("Clase creada:", clase)
            pausar()

        elif opcion == "2":
            hoy = date.today()
            clases_hoy = clases_srv.clases_de_hoy(hoy)
            if not clases_hoy:
                print("No hay clases para hoy.")
            else:
                print(f"Clases del día {hoy}:")
                lineas = [str(c) for c in clases_hoy]
                listado = Formateadores.formatear_lista_simples(lineas)
                print(listado)
            pausar()

        elif opcion == "3":
            clase_id = input("ID de la clase: ").strip()
            dni = input("DNI del miembro: ").strip()
            try:
                clase_id_int = int(clase_id)
            except ValueError:
                print("ID de clase inválido.")
                pausar()
                continue
            socio = socios_srv.buscar_por_dni(dni)
            if not socio:
                print("Miembro no encontrado.")
                pausar()
                continue
            try:
                clases_srv.inscribir_socio(clase_id_int, socio)
                print("Miembro inscrito correctamente en la clase.")
            except Exception as e:
                print(f"No se pudo inscribir: {e}")
            pausar()

        elif opcion == "4":
            clase_id = input("ID de la clase: ").strip()
            try:
                clase_id_int = int(clase_id)
            except ValueError:
                print("ID inválido.")
                pausar()
                continue
            clase = clases_srv.buscar_por_id(clase_id_int)
            if not clase:
                print("Clase no encontrada.")
            else:
                if not clase.inscritos:
                    print("La clase no tiene inscritos.")
                else:
                    print("Inscritos en la clase:")
                    lineas = [f"{s.nombres} {s.apellidos} (DNI {s.dni})" for s in clase.inscritos]
                    listado = Formateadores.formatear_lista_simples(lineas)
                    print(listado)
            pausar()

        elif opcion == "5":
            break
        else:
            print("Opción inválida.")
            pausar()


if __name__ == "__main__":
    menu_principal()
