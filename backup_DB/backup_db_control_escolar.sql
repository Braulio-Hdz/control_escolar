PGDMP                         |            CONTROL_ESCOLAR    15.3    15.3 ?    ]           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false            ^           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false            _           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false            `           1262    24851    CONTROL_ESCOLAR    DATABASE     �   CREATE DATABASE "CONTROL_ESCOLAR" WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE_PROVIDER = libc LOCALE = 'Spanish_Mexico.1252';
 !   DROP DATABASE "CONTROL_ESCOLAR";
                postgres    false            �            1259    24852    perfiles    TABLE     j   CREATE TABLE public.perfiles (
    id_perfiles integer NOT NULL,
    nombre character varying NOT NULL
);
    DROP TABLE public.perfiles;
       public         heap    postgres    false            �            1259    24859    Perfiles_id_perfiles_seq    SEQUENCE     �   ALTER TABLE public.perfiles ALTER COLUMN id_perfiles ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public."Perfiles_id_perfiles_seq"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);
            public          postgres    false    214            �            1259    24872    alumnos    TABLE     �  CREATE TABLE public.alumnos (
    email character varying(50) NOT NULL,
    nombre character varying(50) NOT NULL,
    apellido_paterno character varying(50) NOT NULL,
    apellido_materno character varying(50),
    fecha_nacimiento date,
    carrera character varying(15) NOT NULL,
    fecha_ingreso date,
    situacion character varying(30),
    codigo character varying(15) NOT NULL
);
    DROP TABLE public.alumnos;
       public         heap    postgres    false            �            1259    24889    areas_estudio    TABLE     p   CREATE TABLE public.areas_estudio (
    id_areas integer NOT NULL,
    nombre character varying(50) NOT NULL
);
 !   DROP TABLE public.areas_estudio;
       public         heap    postgres    false            �            1259    24888    areas_estudio_id_areas_seq    SEQUENCE     �   ALTER TABLE public.areas_estudio ALTER COLUMN id_areas ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public.areas_estudio_id_areas_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);
            public          postgres    false    220            �            1259    24912    areas_maestro    TABLE     n   CREATE TABLE public.areas_maestro (
    areas integer NOT NULL,
    maestro character varying(50) NOT NULL
);
 !   DROP TABLE public.areas_maestro;
       public         heap    postgres    false            �            1259    24930    carreras    TABLE     �   CREATE TABLE public.carreras (
    clave character varying(15) NOT NULL,
    nombre character varying(50) NOT NULL,
    nivel integer NOT NULL
);
    DROP TABLE public.carreras;
       public         heap    postgres    false            �            1259    24945    cursos    TABLE     �   CREATE TABLE public.cursos (
    clave character varying(15) NOT NULL,
    area integer NOT NULL,
    nombre character varying(40) NOT NULL,
    creditos integer,
    carrera character varying(15) NOT NULL
);
    DROP TABLE public.cursos;
       public         heap    postgres    false            �            1259    24960    horarios    TABLE     �   CREATE TABLE public.horarios (
    id integer NOT NULL,
    primer_dia character varying(15) NOT NULL,
    segundo_dia character varying(15) NOT NULL,
    hora_inicio character varying(10),
    hora_fin character varying(10)
);
    DROP TABLE public.horarios;
       public         heap    postgres    false            �            1259    25006    horarios_id_seq    SEQUENCE     �   ALTER TABLE public.horarios ALTER COLUMN id ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public.horarios_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);
            public          postgres    false    227            �            1259    24880    maestros    TABLE     &  CREATE TABLE public.maestros (
    email character varying(50) NOT NULL,
    nombre character varying(50) NOT NULL,
    apellido_paterno character varying(50) NOT NULL,
    apellido_materno character varying(50),
    nivel_estudios character varying(15),
    situacion character varying(15)
);
    DROP TABLE public.maestros;
       public         heap    postgres    false            �            1259    24895    niveles_estudio    TABLE     t   CREATE TABLE public.niveles_estudio (
    id_niveles integer NOT NULL,
    nombre character varying(50) NOT NULL
);
 #   DROP TABLE public.niveles_estudio;
       public         heap    postgres    false            �            1259    24894    niveles_estudio_id_niveles_seq    SEQUENCE     �   ALTER TABLE public.niveles_estudio ALTER COLUMN id_niveles ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public.niveles_estudio_id_niveles_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);
            public          postgres    false    222            �            1259    24965    ofertas    TABLE       CREATE TABLE public.ofertas (
    nrc character varying(15) NOT NULL,
    curso character varying(15) NOT NULL,
    horario integer NOT NULL,
    salon character varying(15) NOT NULL,
    maestro character varying(40),
    fecha_inicio date,
    fecha_fin date
);
    DROP TABLE public.ofertas;
       public         heap    postgres    false            �            1259    24993    registro    TABLE     p   CREATE TABLE public.registro (
    codigo_alumno character varying(20),
    nrc_oferta character varying(15)
);
    DROP TABLE public.registro;
       public         heap    postgres    false            �            1259    24940    salones    TABLE     �   CREATE TABLE public.salones (
    abreviatura character varying(10) NOT NULL,
    edificio character varying(10) NOT NULL,
    aula character varying(10) NOT NULL
);
    DROP TABLE public.salones;
       public         heap    postgres    false            �            1259    24860    usuarios    TABLE     �   CREATE TABLE public.usuarios (
    email character varying NOT NULL,
    password character varying NOT NULL,
    perfil integer NOT NULL
);
    DROP TABLE public.usuarios;
       public         heap    postgres    false            M          0    24872    alumnos 
   TABLE DATA           �   COPY public.alumnos (email, nombre, apellido_paterno, apellido_materno, fecha_nacimiento, carrera, fecha_ingreso, situacion, codigo) FROM stdin;
    public          postgres    false    217   'M       P          0    24889    areas_estudio 
   TABLE DATA           9   COPY public.areas_estudio (id_areas, nombre) FROM stdin;
    public          postgres    false    220   �M       S          0    24912    areas_maestro 
   TABLE DATA           7   COPY public.areas_maestro (areas, maestro) FROM stdin;
    public          postgres    false    223   QN       T          0    24930    carreras 
   TABLE DATA           8   COPY public.carreras (clave, nombre, nivel) FROM stdin;
    public          postgres    false    224   nN       V          0    24945    cursos 
   TABLE DATA           H   COPY public.cursos (clave, area, nombre, creditos, carrera) FROM stdin;
    public          postgres    false    226   �N       W          0    24960    horarios 
   TABLE DATA           V   COPY public.horarios (id, primer_dia, segundo_dia, hora_inicio, hora_fin) FROM stdin;
    public          postgres    false    227   �N       N          0    24880    maestros 
   TABLE DATA           p   COPY public.maestros (email, nombre, apellido_paterno, apellido_materno, nivel_estudios, situacion) FROM stdin;
    public          postgres    false    218   O       R          0    24895    niveles_estudio 
   TABLE DATA           =   COPY public.niveles_estudio (id_niveles, nombre) FROM stdin;
    public          postgres    false    222   iO       X          0    24965    ofertas 
   TABLE DATA           _   COPY public.ofertas (nrc, curso, horario, salon, maestro, fecha_inicio, fecha_fin) FROM stdin;
    public          postgres    false    228   �O       J          0    24852    perfiles 
   TABLE DATA           7   COPY public.perfiles (id_perfiles, nombre) FROM stdin;
    public          postgres    false    214   �O       Y          0    24993    registro 
   TABLE DATA           =   COPY public.registro (codigo_alumno, nrc_oferta) FROM stdin;
    public          postgres    false    229   P       U          0    24940    salones 
   TABLE DATA           >   COPY public.salones (abreviatura, edificio, aula) FROM stdin;
    public          postgres    false    225   %P       L          0    24860    usuarios 
   TABLE DATA           ;   COPY public.usuarios (email, password, perfil) FROM stdin;
    public          postgres    false    216   BP       a           0    0    Perfiles_id_perfiles_seq    SEQUENCE SET     H   SELECT pg_catalog.setval('public."Perfiles_id_perfiles_seq"', 3, true);
          public          postgres    false    215            b           0    0    areas_estudio_id_areas_seq    SEQUENCE SET     I   SELECT pg_catalog.setval('public.areas_estudio_id_areas_seq', 19, true);
          public          postgres    false    219            c           0    0    horarios_id_seq    SEQUENCE SET     >   SELECT pg_catalog.setval('public.horarios_id_seq', 1, false);
          public          postgres    false    230            d           0    0    niveles_estudio_id_niveles_seq    SEQUENCE SET     L   SELECT pg_catalog.setval('public.niveles_estudio_id_niveles_seq', 3, true);
          public          postgres    false    221            �           2606    24858    perfiles Perfiles_pkey 
   CONSTRAINT     _   ALTER TABLE ONLY public.perfiles
    ADD CONSTRAINT "Perfiles_pkey" PRIMARY KEY (id_perfiles);
 B   ALTER TABLE ONLY public.perfiles DROP CONSTRAINT "Perfiles_pkey";
       public            postgres    false    214            �           2606    24911    maestros maestros_pkey 
   CONSTRAINT     W   ALTER TABLE ONLY public.maestros
    ADD CONSTRAINT maestros_pkey PRIMARY KEY (email);
 @   ALTER TABLE ONLY public.maestros DROP CONSTRAINT maestros_pkey;
       public            postgres    false    218            �           2606    24909    alumnos pk_alumnos_codigo 
   CONSTRAINT     [   ALTER TABLE ONLY public.alumnos
    ADD CONSTRAINT pk_alumnos_codigo PRIMARY KEY (codigo);
 C   ALTER TABLE ONLY public.alumnos DROP CONSTRAINT pk_alumnos_codigo;
       public            postgres    false    217            �           2606    24893    areas_estudio pk_areas_id 
   CONSTRAINT     ]   ALTER TABLE ONLY public.areas_estudio
    ADD CONSTRAINT pk_areas_id PRIMARY KEY (id_areas);
 C   ALTER TABLE ONLY public.areas_estudio DROP CONSTRAINT pk_areas_id;
       public            postgres    false    220            �           2606    24934    carreras pk_carrera_clave 
   CONSTRAINT     Z   ALTER TABLE ONLY public.carreras
    ADD CONSTRAINT pk_carrera_clave PRIMARY KEY (clave);
 C   ALTER TABLE ONLY public.carreras DROP CONSTRAINT pk_carrera_clave;
       public            postgres    false    224            �           2606    24949    cursos pk_curso_clave 
   CONSTRAINT     V   ALTER TABLE ONLY public.cursos
    ADD CONSTRAINT pk_curso_clave PRIMARY KEY (clave);
 ?   ALTER TABLE ONLY public.cursos DROP CONSTRAINT pk_curso_clave;
       public            postgres    false    226            �           2606    24964    horarios pk_horario_id 
   CONSTRAINT     T   ALTER TABLE ONLY public.horarios
    ADD CONSTRAINT pk_horario_id PRIMARY KEY (id);
 @   ALTER TABLE ONLY public.horarios DROP CONSTRAINT pk_horario_id;
       public            postgres    false    227            �           2606    24899 %   niveles_estudio pk_niveles_estudio_id 
   CONSTRAINT     k   ALTER TABLE ONLY public.niveles_estudio
    ADD CONSTRAINT pk_niveles_estudio_id PRIMARY KEY (id_niveles);
 O   ALTER TABLE ONLY public.niveles_estudio DROP CONSTRAINT pk_niveles_estudio_id;
       public            postgres    false    222            �           2606    24969    ofertas pk_oferta_nrc 
   CONSTRAINT     T   ALTER TABLE ONLY public.ofertas
    ADD CONSTRAINT pk_oferta_nrc PRIMARY KEY (nrc);
 ?   ALTER TABLE ONLY public.ofertas DROP CONSTRAINT pk_oferta_nrc;
       public            postgres    false    228            �           2606    24944    salones pk_salon_abreviatura 
   CONSTRAINT     c   ALTER TABLE ONLY public.salones
    ADD CONSTRAINT pk_salon_abreviatura PRIMARY KEY (abreviatura);
 F   ALTER TABLE ONLY public.salones DROP CONSTRAINT pk_salon_abreviatura;
       public            postgres    false    225            �           2606    24866    usuarios pk_usuarios_email 
   CONSTRAINT     [   ALTER TABLE ONLY public.usuarios
    ADD CONSTRAINT pk_usuarios_email PRIMARY KEY (email);
 D   ALTER TABLE ONLY public.usuarios DROP CONSTRAINT pk_usuarios_email;
       public            postgres    false    216            �           2606    24875    alumnos fk_alumnos_email    FK CONSTRAINT     �   ALTER TABLE ONLY public.alumnos
    ADD CONSTRAINT fk_alumnos_email FOREIGN KEY (email) REFERENCES public.usuarios(email) ON UPDATE CASCADE ON DELETE CASCADE;
 B   ALTER TABLE ONLY public.alumnos DROP CONSTRAINT fk_alumnos_email;
       public          postgres    false    216    3227    217            �           2606    24950    cursos fk_area_id    FK CONSTRAINT     �   ALTER TABLE ONLY public.cursos
    ADD CONSTRAINT fk_area_id FOREIGN KEY (area) REFERENCES public.areas_estudio(id_areas) ON UPDATE CASCADE ON DELETE CASCADE;
 ;   ALTER TABLE ONLY public.cursos DROP CONSTRAINT fk_area_id;
       public          postgres    false    220    3233    226            �           2606    24915    areas_maestro fk_areas_id    FK CONSTRAINT     �   ALTER TABLE ONLY public.areas_maestro
    ADD CONSTRAINT fk_areas_id FOREIGN KEY (areas) REFERENCES public.areas_estudio(id_areas) ON UPDATE CASCADE ON DELETE CASCADE;
 C   ALTER TABLE ONLY public.areas_maestro DROP CONSTRAINT fk_areas_id;
       public          postgres    false    223    220    3233            �           2606    24955    cursos fk_carrera_clave    FK CONSTRAINT     �   ALTER TABLE ONLY public.cursos
    ADD CONSTRAINT fk_carrera_clave FOREIGN KEY (carrera) REFERENCES public.carreras(clave) ON UPDATE CASCADE ON DELETE CASCADE;
 A   ALTER TABLE ONLY public.cursos DROP CONSTRAINT fk_carrera_clave;
       public          postgres    false    3237    226    224            �           2606    24935    carreras fk_carrera_nivel    FK CONSTRAINT     �   ALTER TABLE ONLY public.carreras
    ADD CONSTRAINT fk_carrera_nivel FOREIGN KEY (nivel) REFERENCES public.niveles_estudio(id_niveles);
 C   ALTER TABLE ONLY public.carreras DROP CONSTRAINT fk_carrera_nivel;
       public          postgres    false    224    3235    222            �           2606    24996    registro fk_codigo_alumo    FK CONSTRAINT     �   ALTER TABLE ONLY public.registro
    ADD CONSTRAINT fk_codigo_alumo FOREIGN KEY (codigo_alumno) REFERENCES public.alumnos(codigo) ON UPDATE CASCADE ON DELETE CASCADE;
 B   ALTER TABLE ONLY public.registro DROP CONSTRAINT fk_codigo_alumo;
       public          postgres    false    217    229    3229            �           2606    24970    ofertas fk_curso_clave    FK CONSTRAINT     �   ALTER TABLE ONLY public.ofertas
    ADD CONSTRAINT fk_curso_clave FOREIGN KEY (curso) REFERENCES public.cursos(clave) ON UPDATE CASCADE ON DELETE CASCADE;
 @   ALTER TABLE ONLY public.ofertas DROP CONSTRAINT fk_curso_clave;
       public          postgres    false    226    228    3241            �           2606    24975    ofertas fk_horario_id    FK CONSTRAINT     �   ALTER TABLE ONLY public.ofertas
    ADD CONSTRAINT fk_horario_id FOREIGN KEY (horario) REFERENCES public.horarios(id) ON UPDATE CASCADE ON DELETE CASCADE;
 ?   ALTER TABLE ONLY public.ofertas DROP CONSTRAINT fk_horario_id;
       public          postgres    false    227    228    3243            �           2606    24920    areas_maestro fk_maestro_email    FK CONSTRAINT     �   ALTER TABLE ONLY public.areas_maestro
    ADD CONSTRAINT fk_maestro_email FOREIGN KEY (maestro) REFERENCES public.maestros(email);
 H   ALTER TABLE ONLY public.areas_maestro DROP CONSTRAINT fk_maestro_email;
       public          postgres    false    223    218    3231            �           2606    24985    ofertas fk_maestro_email    FK CONSTRAINT     �   ALTER TABLE ONLY public.ofertas
    ADD CONSTRAINT fk_maestro_email FOREIGN KEY (maestro) REFERENCES public.maestros(email) ON UPDATE CASCADE ON DELETE CASCADE;
 B   ALTER TABLE ONLY public.ofertas DROP CONSTRAINT fk_maestro_email;
       public          postgres    false    218    3231    228            �           2606    24883    maestros fk_maestros_email    FK CONSTRAINT     �   ALTER TABLE ONLY public.maestros
    ADD CONSTRAINT fk_maestros_email FOREIGN KEY (email) REFERENCES public.usuarios(email) ON UPDATE CASCADE ON DELETE CASCADE;
 D   ALTER TABLE ONLY public.maestros DROP CONSTRAINT fk_maestros_email;
       public          postgres    false    3227    218    216            �           2606    25001    registro fk_nrc_oferta    FK CONSTRAINT     �   ALTER TABLE ONLY public.registro
    ADD CONSTRAINT fk_nrc_oferta FOREIGN KEY (nrc_oferta) REFERENCES public.ofertas(nrc) ON UPDATE CASCADE ON DELETE CASCADE;
 @   ALTER TABLE ONLY public.registro DROP CONSTRAINT fk_nrc_oferta;
       public          postgres    false    3245    228    229            �           2606    24980    ofertas fk_salon_abreviatura    FK CONSTRAINT     �   ALTER TABLE ONLY public.ofertas
    ADD CONSTRAINT fk_salon_abreviatura FOREIGN KEY (salon) REFERENCES public.salones(abreviatura) ON UPDATE CASCADE ON DELETE CASCADE;
 F   ALTER TABLE ONLY public.ofertas DROP CONSTRAINT fk_salon_abreviatura;
       public          postgres    false    225    228    3239            �           2606    24867    usuarios fk_usuarios_perfil    FK CONSTRAINT     �   ALTER TABLE ONLY public.usuarios
    ADD CONSTRAINT fk_usuarios_perfil FOREIGN KEY (perfil) REFERENCES public.perfiles(id_perfiles) ON UPDATE CASCADE ON DELETE SET NULL;
 E   ALTER TABLE ONLY public.usuarios DROP CONSTRAINT fk_usuarios_perfil;
       public          postgres    false    3225    214    216            M   �   x�}̽
�0@���]n���M�U�4C�"N.A3D�#�]|z+�� ��,������a�)W��P�|�ѕd��=a�e�	�I!�H
�0O���+��q?��y��n����}�>�g�H�;�e�i��V5;q��/��2�      P   �   x���1���)�	៑!���%�U�HWi���l��Ϧ9��cb����n:'�o�<�k���s����Vg������S��6��^t�Qi�"�^ m�,��vp��qÑ�p��j���!��0!      S      x������ � �      T   \   x�]�1
� @�YO�Z�*Zq���@M�������>�d��]絾�#���,�!� ȭ�bg�	R�M\����t�Y-:�Zk?�� p      V      x������ � �      W      x������ � �      N   E   x�K�J�-��w�ML-.)��K���t*J,�����H-�K�KI���M,*���4���st������� ���      R   3   x�3���LN�K�L,)-J�2��ML-.)�L�2�t�O.�/JL������ 2�!      X      x������ � �      J   /   x�3�tL����,.)JL�/�2�t�)����2��ML��s��qqq 
y      Y      x������ � �      U      x������ � �      L   [   x�E�;
�  �z�0�H<���d���������M\b��S{jgf�ւ��U�/ih��f�r���>vNkt΁����֔6C��/�{%     