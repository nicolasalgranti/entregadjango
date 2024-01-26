# entrega
Proyecto Fakebook

link video explicación: https://drive.google.com/file/d/18LuClYgo-KrueOnCNwC_8Yp_VPpwDCi9/view?usp=drive_link

Django admin datos:
        nombre: admin
        contraseña: adm12345

Fakebook es una app que pretende en un futuro contar con funciones similares a las de una red social como Facebook. A través de la página de Usuarios, destinada a ayudar a usuarios que no recuerdan si están registrados o no, estos pueden llenar un formulario que, en caso de estar registrados, les señalará su dirección de correo electrónico.

La página staff invita a los usuarios a formar parte del equipo de desarrollo mediante un formulario. El administrador puede acceder a la lista de solicitudes enviadas mediante el url CoderApp/solicitudes/list. Tras leer cada solicitud, puede agregar a los solicitantes al staff tanto mediante el url CoderApp/staff/list como por el sitio de administración integrado de Django. Nótese que solamente pueden acceder a estas funciones miembros del staff. Además de convertir a los usuarios en staff dándoles "staff status" a sus cuentas, consideré importante crear el modelo Staff con el nombre, apellido y correo de cada uno para que queden enlistados en el admin nativo de Django con el fin de tener una mejor organización. En caso de formar parte del staff, se puede acceder al admin nativo de Django mediante un botón situado en el index, debajo del mensaje de bienvenida.

Con el objetivo de mantener la página en constante crecimiento, creé la funcionalidad Sugerencias, a través de la cual los usuarios pueden llenar un mensaje con alguna funcionalidad o cambio que les gustaría ver implementado en la página. Estas sugerencias deben ser leídas a través de la página integrada de administrador de Django. 

El avatar del usuario puede ser agregado a través de la página "editar perfil", que aparece en el extremo superior derecho una vez que inicia sesión. Usé el método order_by('-created_at') en las views "login_request" y "index" con el fin de que el usuario pueda editar su avatar, y que este sea el que haya escogido más recientemente. Tanto el sistema de manejo del staff como el de leer y eliminar las distintas solicitudes fueron implementados a través de métodos CRUD.

Tal como es indicado en la página "Sobre nosotros", el proyecto fue hecho enteramente por mí.

urls importantes para el administrador: CoderApp/solicitudes/list (CRUD de las solicitudes)
                                        CoderApp/staff/list (CRUD del staff)
                                         