# 🚀 STACK TÉCNICO: NEXT.JS + SUPABASE + VERCEL

## 📋 Documento de Arquitectura - PAIDEIA Platform

**Versión**: 1.0
**Fecha**: 29 de Noviembre 2025
**Autor**: Claude (Asistente IA)
**Aprobado por**: Randhy Paul Rodriguez Santos

---

## 📌 ÍNDICE

1. [Resumen Ejecutivo](#1-resumen-ejecutivo)
2. [Stack Tecnológico](#2-stack-tecnológico)
3. [Arquitectura del Sistema](#3-arquitectura-del-sistema)
4. [Estructura del Proyecto](#4-estructura-del-proyecto)
5. [Modelo de Base de Datos](#5-modelo-de-base-de-datos)
6. [Sistema de Autenticación](#6-sistema-de-autenticación)
7. [Feature Premium: IA Asistente](#7-feature-premium-ia-asistente)
8. [Sistema de Progreso y Certificados](#8-sistema-de-progreso-y-certificados)
9. [Deployment y CI/CD](#9-deployment-y-cicd)
10. [Costos y Escalabilidad](#10-costos-y-escalabilidad)
11. [Sprints de Implementación](#11-sprints-de-implementación)

---

## 1. RESUMEN EJECUTIVO

### ¿Por qué este Stack?

**Problema con GitHub Pages:**
- Solo archivos estáticos (HTML, CSS, JS)
- NO soporta backend/servidor
- NO base de datos
- Limitado para autenticación real
- Sin API routes

**Solución: Next.js + Supabase + Vercel**
- Full-stack en un solo framework
- Base de datos PostgreSQL incluida
- Autenticación completa
- Costo $0 para empezar
- Escalable a millones de usuarios

### Comparativa

| Característica | GitHub Pages | Next.js + Supabase |
|---------------|--------------|---------------------|
| Backend | ❌ No | ✅ Sí |
| Base de datos | ❌ No | ✅ PostgreSQL |
| Autenticación | ❌ Manual/limitada | ✅ Completa |
| API Routes | ❌ No | ✅ Sí |
| IA Integration | ❌ No | ✅ Sí |
| Costo inicial | $0 | $0 |
| Escalabilidad | Baja | Alta |
| Certificados dinámicos | ❌ No | ✅ Sí |

---

## 2. STACK TECNOLÓGICO

### 2.1 Frontend: Next.js 14+

```
┌─────────────────────────────────────────────┐
│              NEXT.JS 14                      │
├─────────────────────────────────────────────┤
│  • App Router (nueva arquitectura)          │
│  • Server Components (renderizan en server) │
│  • Client Components (interactividad)       │
│  • API Routes (backend integrado)           │
│  • TypeScript (tipado estático)             │
│  • Tailwind CSS (estilos)                   │
└─────────────────────────────────────────────┘
```

**¿Por qué Next.js?**
- Framework React más popular y maduro
- Rendimiento optimizado (SSR, SSG, ISR)
- Vercel lo creó = integración perfecta
- Documentación excelente
- Gran comunidad

### 2.2 Backend: Supabase

```
┌─────────────────────────────────────────────┐
│              SUPABASE                        │
├─────────────────────────────────────────────┤
│  📦 PostgreSQL (base de datos)              │
│  🔐 Auth (autenticación)                    │
│  📁 Storage (archivos/imágenes)             │
│  ⚡ Realtime (actualizaciones en vivo)      │
│  🔌 Edge Functions (serverless)             │
└─────────────────────────────────────────────┘
```

**¿Por qué Supabase?**
- "Firebase de código abierto"
- PostgreSQL (el mejor SQL)
- Autenticación lista para usar
- SDK simple para JavaScript
- Tier gratuito generoso
- Self-hosteable si necesario

### 2.3 Hosting: Vercel

```
┌─────────────────────────────────────────────┐
│              VERCEL                          │
├─────────────────────────────────────────────┤
│  🌐 CDN Global (rápido en todo el mundo)    │
│  🔄 CI/CD Automático (push = deploy)        │
│  📊 Analytics (métricas de uso)             │
│  🔒 HTTPS automático                        │
│  💰 Tier gratuito generoso                  │
└─────────────────────────────────────────────┘
```

### 2.4 IA: Claude API (Anthropic)

```
┌─────────────────────────────────────────────┐
│              CLAUDE API                      │
├─────────────────────────────────────────────┤
│  🧠 Modelo: Claude 3.5 Sonnet               │
│  💬 Asistente contextual                    │
│  📚 Conocimiento del contenido del curso    │
│  🎯 Restricción por nivel de estudiante     │
└─────────────────────────────────────────────┘
```

---

## 3. ARQUITECTURA DEL SISTEMA

### 3.1 Diagrama General

```
                    ┌─────────────────┐
                    │   USUARIO       │
                    │   (Navegador)   │
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │    VERCEL       │
                    │    (Hosting)    │
                    └────────┬────────┘
                             │
              ┌──────────────┼──────────────┐
              │              │              │
              ▼              ▼              ▼
     ┌────────────┐  ┌────────────┐  ┌────────────┐
     │  NEXT.JS   │  │  NEXT.JS   │  │  NEXT.JS   │
     │   Pages    │  │    API     │  │  Server    │
     │ (Frontend) │  │   Routes   │  │ Components │
     └──────┬─────┘  └──────┬─────┘  └──────┬─────┘
            │               │               │
            └───────────────┼───────────────┘
                            │
              ┌─────────────┼─────────────┐
              │             │             │
              ▼             ▼             ▼
     ┌────────────┐  ┌────────────┐  ┌────────────┐
     │  SUPABASE  │  │  SUPABASE  │  │  CLAUDE    │
     │    Auth    │  │  Database  │  │    API     │
     └────────────┘  └────────────┘  └────────────┘
```

### 3.2 Flujo de Usuario

```
┌──────────────────────────────────────────────────────────────────┐
│                    FLUJO DE USUARIO PAIDEIA                       │
└──────────────────────────────────────────────────────────────────┘

1. LANDING PAGE (público)
   │
   ├─→ [Empezar Gratis] ──→ Quiz de Perfil ──→ Registro
   │
   └─→ [Ya tengo cuenta] ──→ Login

2. REGISTRO/LOGIN
   │
   ├─→ Email + Contraseña
   ├─→ Google OAuth
   └─→ GitHub OAuth (para programadores)

3. ONBOARDING (primera vez)
   │
   ├─→ Quiz de perfil profesional
   ├─→ Asignación de ruta personalizada
   └─→ Dashboard personalizado

4. DASHBOARD
   │
   ├─→ Ver progreso actual
   ├─→ Continuar donde quedó
   ├─→ Ver módulos desbloqueados
   └─→ Chatear con IA Asistente (Premium)

5. MÓDULO DE ESTUDIO
   │
   ├─→ Video/Contenido
   ├─→ Ejercicios prácticos
   ├─→ Quiz de evaluación
   └─→ Marcar como completado

6. CERTIFICACIÓN
   │
   ├─→ Examen final
   ├─→ Generación de certificado PDF
   └─→ Código de verificación único
```

---

## 4. ESTRUCTURA DEL PROYECTO

### 4.1 Árbol de Directorios

```
paideia-platform/
│
├── 📁 app/                          # App Router (Next.js 14)
│   │
│   ├── 📁 (auth)/                   # Grupo de rutas de autenticación
│   │   ├── 📁 login/
│   │   │   └── page.tsx             # /login
│   │   ├── 📁 registro/
│   │   │   └── page.tsx             # /registro
│   │   └── 📁 recuperar/
│   │       └── page.tsx             # /recuperar-contraseña
│   │
│   ├── 📁 (app)/                    # Grupo de rutas protegidas
│   │   ├── 📁 dashboard/
│   │   │   └── page.tsx             # /dashboard
│   │   ├── 📁 perfil/
│   │   │   └── page.tsx             # /perfil
│   │   ├── 📁 nivel/
│   │   │   └── 📁 [id]/
│   │   │       └── page.tsx         # /nivel/1, /nivel/2, etc.
│   │   ├── 📁 modulo/
│   │   │   └── 📁 [id]/
│   │   │       └── page.tsx         # /modulo/fundamentos-pm
│   │   ├── 📁 quiz/
│   │   │   └── 📁 [id]/
│   │   │       └── page.tsx         # /quiz/evaluacion-nivel-1
│   │   ├── 📁 certificado/
│   │   │   └── page.tsx             # /certificado
│   │   └── 📁 asistente/
│   │       └── page.tsx             # /asistente (IA Chat - Premium)
│   │
│   ├── 📁 api/                      # API Routes (Backend)
│   │   ├── 📁 auth/
│   │   │   └── route.ts             # Webhooks de autenticación
│   │   ├── 📁 progreso/
│   │   │   └── route.ts             # CRUD de progreso
│   │   ├── 📁 certificado/
│   │   │   └── route.ts             # Generar certificados
│   │   ├── 📁 quiz/
│   │   │   └── route.ts             # Evaluar respuestas
│   │   └── 📁 asistente/
│   │       └── route.ts             # IA Asistente API
│   │
│   ├── layout.tsx                   # Layout raíz
│   ├── page.tsx                     # Landing page (/)
│   └── globals.css                  # Estilos globales
│
├── 📁 components/                   # Componentes reutilizables
│   ├── 📁 ui/                       # Componentes de UI base
│   │   ├── Button.tsx
│   │   ├── Card.tsx
│   │   ├── Input.tsx
│   │   ├── Modal.tsx
│   │   └── Progress.tsx
│   ├── 📁 layout/                   # Componentes de estructura
│   │   ├── Navbar.tsx
│   │   ├── Sidebar.tsx
│   │   └── Footer.tsx
│   ├── 📁 features/                 # Componentes de funcionalidad
│   │   ├── QuizPerfil.tsx
│   │   ├── ModuloCard.tsx
│   │   ├── ProgresoCircular.tsx
│   │   ├── CertificadoViewer.tsx
│   │   └── ChatAsistente.tsx
│   └── 📁 icons/                    # Iconos SVG
│       └── index.tsx
│
├── 📁 lib/                          # Utilidades y configuraciones
│   ├── supabase/
│   │   ├── client.ts                # Cliente Supabase (browser)
│   │   ├── server.ts                # Cliente Supabase (server)
│   │   └── admin.ts                 # Cliente Supabase (admin)
│   ├── claude/
│   │   └── client.ts                # Cliente Claude API
│   ├── utils.ts                     # Funciones utilitarias
│   └── constants.ts                 # Constantes globales
│
├── 📁 hooks/                        # Custom React Hooks
│   ├── useUser.ts                   # Hook de usuario actual
│   ├── useProgreso.ts               # Hook de progreso
│   └── useAsistente.ts              # Hook de chat IA
│
├── 📁 types/                        # Definiciones TypeScript
│   ├── database.ts                  # Tipos generados de Supabase
│   ├── user.ts
│   ├── modulo.ts
│   └── quiz.ts
│
├── 📁 content/                      # Contenido del curso (MDX)
│   ├── 📁 nivel-0/
│   │   └── despertar.mdx
│   ├── 📁 nivel-1/
│   │   ├── fundamentos-pm.mdx
│   │   └── ciclo-vida-proyecto.mdx
│   ├── 📁 nivel-2/
│   │   ├── prompt-engineering.mdx
│   │   └── herramientas-ia.mdx
│   └── ...
│
├── 📁 public/                       # Archivos estáticos
│   ├── 📁 images/
│   ├── 📁 icons/
│   └── 📁 fonts/
│
├── 📁 supabase/                     # Configuración Supabase
│   ├── 📁 migrations/               # Migraciones de BD
│   │   ├── 001_initial_schema.sql
│   │   ├── 002_add_progreso.sql
│   │   └── 003_add_certificados.sql
│   └── config.toml
│
├── .env.local                       # Variables de entorno (local)
├── .env.example                     # Ejemplo de variables
├── next.config.js                   # Configuración Next.js
├── tailwind.config.js               # Configuración Tailwind
├── tsconfig.json                    # Configuración TypeScript
├── package.json                     # Dependencias
└── README.md                        # Documentación
```

### 4.2 Dependencias Principales

```json
{
  "dependencies": {
    "next": "^14.0.0",
    "react": "^18.2.0",
    "react-dom": "^18.2.0",
    "@supabase/supabase-js": "^2.38.0",
    "@supabase/auth-helpers-nextjs": "^0.8.0",
    "@anthropic-ai/sdk": "^0.9.0",
    "tailwindcss": "^3.3.0",
    "lucide-react": "^0.292.0",
    "date-fns": "^2.30.0",
    "zod": "^3.22.0",
    "jspdf": "^2.5.0"
  },
  "devDependencies": {
    "typescript": "^5.2.0",
    "@types/react": "^18.2.0",
    "@types/node": "^20.0.0",
    "supabase": "^1.100.0"
  }
}
```

---

## 5. MODELO DE BASE DE DATOS

### 5.1 Diagrama Entidad-Relación

```
┌─────────────────────────────────────────────────────────────────────────┐
│                        MODELO DE DATOS PAIDEIA                           │
└─────────────────────────────────────────────────────────────────────────┘

┌──────────────────┐       ┌──────────────────┐       ┌──────────────────┐
│    perfiles      │       │     progreso     │       │   certificados   │
├──────────────────┤       ├──────────────────┤       ├──────────────────┤
│ id (PK)          │──┐    │ id (PK)          │   ┌──│ id (PK)          │
│ auth_id (FK)     │  │    │ user_id (FK)     │───┤  │ user_id (FK)     │
│ email            │  └───→│ nivel_id         │   │  │ tipo_certificado │
│ nombre           │       │ modulo_id        │   │  │ codigo_verificar │
│ perfil_tipo      │       │ completado       │   │  │ fecha_emision    │
│ nivel_actual     │       │ puntaje_quiz     │   │  │ pdf_url          │
│ plan             │       │ fecha_completado │   │  │ metadata (JSON)  │
│ fecha_registro   │       │ tiempo_dedicado  │   │  └──────────────────┘
│ metadata (JSON)  │       └──────────────────┘   │
└──────────────────┘                              │  ┌──────────────────┐
        │                                         │  │  quiz_resultados │
        │          ┌──────────────────┐           │  ├──────────────────┤
        │          │   quiz_perfil    │           └─→│ id (PK)          │
        │          ├──────────────────┤              │ user_id (FK)     │
        └─────────→│ id (PK)          │              │ quiz_id          │
                   │ user_id (FK)     │              │ respuestas (JSON)│
                   │ respuestas (JSON)│              │ puntaje          │
                   │ perfil_resultado │              │ aprobado         │
                   │ fecha            │              │ intentos         │
                   └──────────────────┘              │ fecha            │
                                                     └──────────────────┘

┌──────────────────┐       ┌──────────────────┐
│ chat_asistente   │       │   suscripciones  │
├──────────────────┤       ├──────────────────┤
│ id (PK)          │       │ id (PK)          │
│ user_id (FK)     │       │ user_id (FK)     │
│ mensaje          │       │ plan             │
│ rol (user/ai)    │       │ estado           │
│ contexto (JSON)  │       │ fecha_inicio     │
│ tokens_usados    │       │ fecha_fin        │
│ timestamp        │       │ stripe_id        │
└──────────────────┘       └──────────────────┘
```

### 5.2 SQL de Creación (Migraciones)

```sql
-- ============================================
-- MIGRACIÓN 001: SCHEMA INICIAL
-- ============================================

-- Habilitar extensiones necesarias
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

-- Tipos ENUM
CREATE TYPE perfil_tipo AS ENUM (
    'programador',
    'empresario',
    'contador',
    'marketer',
    'vendedor',
    'pm',
    'disenador',
    'estudiante'
);

CREATE TYPE plan_tipo AS ENUM (
    'gratuito',
    'premium',
    'enterprise'
);

CREATE TYPE certificado_tipo AS ENUM (
    'nivel_completado',
    'especializacion',
    'master_paideia'
);

-- ============================================
-- TABLA: perfiles
-- ============================================
CREATE TABLE perfiles (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    auth_id UUID REFERENCES auth.users(id) ON DELETE CASCADE,
    email TEXT UNIQUE NOT NULL,
    nombre TEXT,
    perfil_tipo perfil_tipo DEFAULT 'estudiante',
    nivel_actual INTEGER DEFAULT 0,
    plan plan_tipo DEFAULT 'gratuito',
    fecha_registro TIMESTAMPTZ DEFAULT NOW(),
    ultima_actividad TIMESTAMPTZ DEFAULT NOW(),
    metadata JSONB DEFAULT '{}',

    CONSTRAINT email_format CHECK (email ~* '^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$')
);

-- Índices
CREATE INDEX idx_perfiles_auth_id ON perfiles(auth_id);
CREATE INDEX idx_perfiles_email ON perfiles(email);
CREATE INDEX idx_perfiles_perfil_tipo ON perfiles(perfil_tipo);

-- ============================================
-- TABLA: progreso
-- ============================================
CREATE TABLE progreso (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    user_id UUID REFERENCES perfiles(id) ON DELETE CASCADE,
    nivel_id TEXT NOT NULL,
    modulo_id TEXT NOT NULL,
    completado BOOLEAN DEFAULT FALSE,
    puntaje_quiz INTEGER,
    fecha_inicio TIMESTAMPTZ DEFAULT NOW(),
    fecha_completado TIMESTAMPTZ,
    tiempo_dedicado INTEGER DEFAULT 0, -- en segundos

    UNIQUE(user_id, nivel_id, modulo_id)
);

-- Índices
CREATE INDEX idx_progreso_user ON progreso(user_id);
CREATE INDEX idx_progreso_nivel ON progreso(nivel_id);
CREATE INDEX idx_progreso_completado ON progreso(completado);

-- ============================================
-- TABLA: quiz_perfil (quiz inicial)
-- ============================================
CREATE TABLE quiz_perfil (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    user_id UUID REFERENCES perfiles(id) ON DELETE CASCADE,
    respuestas JSONB NOT NULL,
    perfil_resultado perfil_tipo NOT NULL,
    fecha TIMESTAMPTZ DEFAULT NOW()
);

-- ============================================
-- TABLA: quiz_resultados (evaluaciones)
-- ============================================
CREATE TABLE quiz_resultados (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    user_id UUID REFERENCES perfiles(id) ON DELETE CASCADE,
    quiz_id TEXT NOT NULL,
    nivel_id TEXT NOT NULL,
    respuestas JSONB NOT NULL,
    puntaje INTEGER NOT NULL,
    puntaje_maximo INTEGER NOT NULL,
    aprobado BOOLEAN DEFAULT FALSE,
    intentos INTEGER DEFAULT 1,
    fecha TIMESTAMPTZ DEFAULT NOW(),

    CONSTRAINT puntaje_valido CHECK (puntaje >= 0 AND puntaje <= puntaje_maximo)
);

-- Índices
CREATE INDEX idx_quiz_user ON quiz_resultados(user_id);
CREATE INDEX idx_quiz_nivel ON quiz_resultados(nivel_id);

-- ============================================
-- TABLA: certificados
-- ============================================
CREATE TABLE certificados (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    user_id UUID REFERENCES perfiles(id) ON DELETE CASCADE,
    tipo_certificado certificado_tipo NOT NULL,
    nivel_id TEXT,
    codigo_verificacion TEXT UNIQUE NOT NULL,
    fecha_emision TIMESTAMPTZ DEFAULT NOW(),
    pdf_url TEXT,
    metadata JSONB DEFAULT '{}'
);

-- Índices
CREATE INDEX idx_cert_user ON certificados(user_id);
CREATE INDEX idx_cert_codigo ON certificados(codigo_verificacion);

-- ============================================
-- TABLA: chat_asistente (historial de IA)
-- ============================================
CREATE TABLE chat_asistente (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    user_id UUID REFERENCES perfiles(id) ON DELETE CASCADE,
    mensaje TEXT NOT NULL,
    rol TEXT NOT NULL CHECK (rol IN ('user', 'assistant')),
    contexto JSONB DEFAULT '{}', -- nivel actual, módulo, etc.
    tokens_usados INTEGER DEFAULT 0,
    timestamp TIMESTAMPTZ DEFAULT NOW()
);

-- Índices
CREATE INDEX idx_chat_user ON chat_asistente(user_id);
CREATE INDEX idx_chat_timestamp ON chat_asistente(timestamp);

-- ============================================
-- TABLA: suscripciones
-- ============================================
CREATE TABLE suscripciones (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    user_id UUID REFERENCES perfiles(id) ON DELETE CASCADE,
    plan plan_tipo NOT NULL,
    estado TEXT DEFAULT 'activo' CHECK (estado IN ('activo', 'cancelado', 'expirado')),
    fecha_inicio TIMESTAMPTZ DEFAULT NOW(),
    fecha_fin TIMESTAMPTZ,
    stripe_customer_id TEXT,
    stripe_subscription_id TEXT,
    metadata JSONB DEFAULT '{}'
);

-- ============================================
-- ROW LEVEL SECURITY (RLS)
-- ============================================

-- Habilitar RLS en todas las tablas
ALTER TABLE perfiles ENABLE ROW LEVEL SECURITY;
ALTER TABLE progreso ENABLE ROW LEVEL SECURITY;
ALTER TABLE quiz_perfil ENABLE ROW LEVEL SECURITY;
ALTER TABLE quiz_resultados ENABLE ROW LEVEL SECURITY;
ALTER TABLE certificados ENABLE ROW LEVEL SECURITY;
ALTER TABLE chat_asistente ENABLE ROW LEVEL SECURITY;
ALTER TABLE suscripciones ENABLE ROW LEVEL SECURITY;

-- Políticas para perfiles
CREATE POLICY "Usuarios pueden ver su propio perfil"
    ON perfiles FOR SELECT
    USING (auth.uid() = auth_id);

CREATE POLICY "Usuarios pueden actualizar su propio perfil"
    ON perfiles FOR UPDATE
    USING (auth.uid() = auth_id);

-- Políticas para progreso
CREATE POLICY "Usuarios pueden ver su propio progreso"
    ON progreso FOR SELECT
    USING (user_id IN (SELECT id FROM perfiles WHERE auth_id = auth.uid()));

CREATE POLICY "Usuarios pueden insertar su propio progreso"
    ON progreso FOR INSERT
    WITH CHECK (user_id IN (SELECT id FROM perfiles WHERE auth_id = auth.uid()));

CREATE POLICY "Usuarios pueden actualizar su propio progreso"
    ON progreso FOR UPDATE
    USING (user_id IN (SELECT id FROM perfiles WHERE auth_id = auth.uid()));

-- (Políticas similares para otras tablas...)

-- ============================================
-- FUNCIONES Y TRIGGERS
-- ============================================

-- Función para crear perfil automáticamente al registrarse
CREATE OR REPLACE FUNCTION handle_new_user()
RETURNS TRIGGER AS $$
BEGIN
    INSERT INTO perfiles (auth_id, email, nombre)
    VALUES (NEW.id, NEW.email, NEW.raw_user_meta_data->>'nombre');
    RETURN NEW;
END;
$$ LANGUAGE plpgsql SECURITY DEFINER;

-- Trigger para crear perfil
CREATE TRIGGER on_auth_user_created
    AFTER INSERT ON auth.users
    FOR EACH ROW EXECUTE FUNCTION handle_new_user();

-- Función para actualizar nivel_actual basado en progreso
CREATE OR REPLACE FUNCTION actualizar_nivel_usuario()
RETURNS TRIGGER AS $$
DECLARE
    nuevo_nivel INTEGER;
BEGIN
    -- Calcular el nivel máximo completado
    SELECT COALESCE(MAX(CAST(SUBSTRING(nivel_id FROM 'nivel-(\d+)') AS INTEGER)), 0)
    INTO nuevo_nivel
    FROM progreso
    WHERE user_id = NEW.user_id
    AND completado = TRUE;

    -- Actualizar el perfil
    UPDATE perfiles
    SET nivel_actual = nuevo_nivel,
        ultima_actividad = NOW()
    WHERE id = NEW.user_id;

    RETURN NEW;
END;
$$ LANGUAGE plpgsql SECURITY DEFINER;

-- Trigger para actualizar nivel
CREATE TRIGGER on_progreso_completado
    AFTER UPDATE OF completado ON progreso
    FOR EACH ROW
    WHEN (NEW.completado = TRUE)
    EXECUTE FUNCTION actualizar_nivel_usuario();

-- Función para generar código de verificación único
CREATE OR REPLACE FUNCTION generar_codigo_verificacion()
RETURNS TEXT AS $$
DECLARE
    codigo TEXT;
    existe BOOLEAN;
BEGIN
    LOOP
        -- Generar código: PAIDEIA-XXXX-XXXX-XXXX
        codigo := 'PAIDEIA-' ||
                  UPPER(SUBSTRING(MD5(RANDOM()::TEXT) FROM 1 FOR 4)) || '-' ||
                  UPPER(SUBSTRING(MD5(RANDOM()::TEXT) FROM 1 FOR 4)) || '-' ||
                  UPPER(SUBSTRING(MD5(RANDOM()::TEXT) FROM 1 FOR 4));

        -- Verificar que no existe
        SELECT EXISTS(SELECT 1 FROM certificados WHERE codigo_verificacion = codigo)
        INTO existe;

        EXIT WHEN NOT existe;
    END LOOP;

    RETURN codigo;
END;
$$ LANGUAGE plpgsql;
```

---

## 6. SISTEMA DE AUTENTICACIÓN

### 6.1 Configuración Supabase Auth

```typescript
// lib/supabase/client.ts
import { createBrowserClient } from '@supabase/ssr'

export function createClient() {
  return createBrowserClient(
    process.env.NEXT_PUBLIC_SUPABASE_URL!,
    process.env.NEXT_PUBLIC_SUPABASE_ANON_KEY!
  )
}
```

```typescript
// lib/supabase/server.ts
import { createServerClient, type CookieOptions } from '@supabase/ssr'
import { cookies } from 'next/headers'

export function createServerSupabase() {
  const cookieStore = cookies()

  return createServerClient(
    process.env.NEXT_PUBLIC_SUPABASE_URL!,
    process.env.NEXT_PUBLIC_SUPABASE_ANON_KEY!,
    {
      cookies: {
        get(name: string) {
          return cookieStore.get(name)?.value
        },
        set(name: string, value: string, options: CookieOptions) {
          cookieStore.set({ name, value, ...options })
        },
        remove(name: string, options: CookieOptions) {
          cookieStore.set({ name, value: '', ...options })
        },
      },
    }
  )
}
```

### 6.2 Flujo de Autenticación

```typescript
// app/(auth)/registro/page.tsx
'use client'

import { useState } from 'react'
import { createClient } from '@/lib/supabase/client'
import { useRouter } from 'next/navigation'

export default function RegistroPage() {
  const [email, setEmail] = useState('')
  const [password, setPassword] = useState('')
  const [nombre, setNombre] = useState('')
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState<string | null>(null)

  const router = useRouter()
  const supabase = createClient()

  const handleRegistro = async (e: React.FormEvent) => {
    e.preventDefault()
    setLoading(true)
    setError(null)

    try {
      const { data, error } = await supabase.auth.signUp({
        email,
        password,
        options: {
          data: {
            nombre: nombre,
          },
          emailRedirectTo: `${window.location.origin}/auth/callback`,
        },
      })

      if (error) throw error

      // Redirigir al quiz de perfil
      router.push('/quiz-perfil')

    } catch (err: any) {
      setError(err.message)
    } finally {
      setLoading(false)
    }
  }

  const handleGoogleLogin = async () => {
    const { error } = await supabase.auth.signInWithOAuth({
      provider: 'google',
      options: {
        redirectTo: `${window.location.origin}/auth/callback`,
      },
    })
    if (error) setError(error.message)
  }

  return (
    <div className="min-h-screen flex items-center justify-center bg-gray-50">
      <div className="max-w-md w-full space-y-8 p-8 bg-white rounded-xl shadow-lg">
        <div>
          <h2 className="text-3xl font-bold text-center text-gray-900">
            Únete a PAIDEIA
          </h2>
          <p className="mt-2 text-center text-gray-600">
            Comienza tu transformación con IA
          </p>
        </div>

        <form onSubmit={handleRegistro} className="space-y-6">
          {error && (
            <div className="bg-red-50 text-red-500 p-3 rounded-lg text-sm">
              {error}
            </div>
          )}

          <div>
            <label htmlFor="nombre" className="block text-sm font-medium">
              Nombre completo
            </label>
            <input
              id="nombre"
              type="text"
              value={nombre}
              onChange={(e) => setNombre(e.target.value)}
              className="mt-1 block w-full rounded-lg border border-gray-300 px-3 py-2"
              required
            />
          </div>

          <div>
            <label htmlFor="email" className="block text-sm font-medium">
              Email
            </label>
            <input
              id="email"
              type="email"
              value={email}
              onChange={(e) => setEmail(e.target.value)}
              className="mt-1 block w-full rounded-lg border border-gray-300 px-3 py-2"
              required
            />
          </div>

          <div>
            <label htmlFor="password" className="block text-sm font-medium">
              Contraseña
            </label>
            <input
              id="password"
              type="password"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
              className="mt-1 block w-full rounded-lg border border-gray-300 px-3 py-2"
              minLength={8}
              required
            />
          </div>

          <button
            type="submit"
            disabled={loading}
            className="w-full flex justify-center py-3 px-4 rounded-lg text-white bg-blue-600 hover:bg-blue-700 disabled:opacity-50"
          >
            {loading ? 'Creando cuenta...' : 'Crear cuenta'}
          </button>
        </form>

        <div className="relative">
          <div className="absolute inset-0 flex items-center">
            <div className="w-full border-t border-gray-300" />
          </div>
          <div className="relative flex justify-center text-sm">
            <span className="px-2 bg-white text-gray-500">O continúa con</span>
          </div>
        </div>

        <button
          onClick={handleGoogleLogin}
          className="w-full flex items-center justify-center gap-3 py-3 px-4 rounded-lg border border-gray-300 hover:bg-gray-50"
        >
          <svg className="w-5 h-5" viewBox="0 0 24 24">
            {/* Google icon SVG */}
          </svg>
          Google
        </button>
      </div>
    </div>
  )
}
```

### 6.3 Middleware de Protección

```typescript
// middleware.ts
import { createServerClient, type CookieOptions } from '@supabase/ssr'
import { NextResponse, type NextRequest } from 'next/server'

export async function middleware(request: NextRequest) {
  let response = NextResponse.next({
    request: {
      headers: request.headers,
    },
  })

  const supabase = createServerClient(
    process.env.NEXT_PUBLIC_SUPABASE_URL!,
    process.env.NEXT_PUBLIC_SUPABASE_ANON_KEY!,
    {
      cookies: {
        get(name: string) {
          return request.cookies.get(name)?.value
        },
        set(name: string, value: string, options: CookieOptions) {
          response.cookies.set({ name, value, ...options })
        },
        remove(name: string, options: CookieOptions) {
          response.cookies.set({ name, value: '', ...options })
        },
      },
    }
  )

  const { data: { user } } = await supabase.auth.getUser()

  // Rutas protegidas
  const protectedRoutes = ['/dashboard', '/perfil', '/nivel', '/modulo', '/asistente']
  const isProtectedRoute = protectedRoutes.some(route =>
    request.nextUrl.pathname.startsWith(route)
  )

  // Si no está autenticado y quiere acceder a ruta protegida
  if (!user && isProtectedRoute) {
    return NextResponse.redirect(new URL('/login', request.url))
  }

  // Si está autenticado y quiere acceder a login/registro
  if (user && (request.nextUrl.pathname === '/login' || request.nextUrl.pathname === '/registro')) {
    return NextResponse.redirect(new URL('/dashboard', request.url))
  }

  return response
}

export const config = {
  matcher: [
    '/((?!_next/static|_next/image|favicon.ico|.*\\.(?:svg|png|jpg|jpeg|gif|webp)$).*)',
  ],
}
```

---

## 7. FEATURE PREMIUM: IA ASISTENTE

### 7.1 Concepto

El **IA Asistente PAIDEIA** es un chatbot inteligente que:
- Conoce todo el contenido del curso
- Consulta el nivel actual del estudiante
- NO ayuda con temas de niveles superiores
- Refuerza el aprendizaje del nivel actual
- Responde dudas de forma pedagógica

### 7.2 Arquitectura del Asistente

```
┌─────────────────────────────────────────────────────────────────┐
│                    IA ASISTENTE PAIDEIA                          │
└─────────────────────────────────────────────────────────────────┘

                    ┌─────────────────┐
                    │   ESTUDIANTE    │
                    │   (Usuario)     │
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │   ChatInterface │
                    │   (Frontend)    │
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │   API Route     │
                    │  /api/asistente │
                    └────────┬────────┘
                             │
           ┌─────────────────┼─────────────────┐
           │                 │                 │
           ▼                 ▼                 ▼
    ┌────────────┐   ┌────────────┐   ┌────────────┐
    │  Supabase  │   │  Context   │   │  Claude    │
    │  (Nivel    │   │  Builder   │   │    API     │
    │  Usuario)  │   │            │   │            │
    └────────────┘   └────────────┘   └────────────┘
           │                 │                 │
           └─────────────────┼─────────────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │   RESPUESTA     │
                    │   CONTROLADA    │
                    └─────────────────┘
```

### 7.3 Lógica de Restricción por Nivel

```typescript
// lib/claude/context-builder.ts

interface UserContext {
  userId: string;
  nombre: string;
  nivelActual: number;
  perfilTipo: string;
  modulosCompletados: string[];
  moduloActual: string | null;
}

interface ContentContext {
  nivelesPermitidos: string[];
  contenidoNivelActual: string;
  contenidoModuloActual: string;
}

export function buildSystemPrompt(user: UserContext, content: ContentContext): string {
  return `
Eres PAIDEIA Assistant, el tutor de IA de la plataforma PAIDEIA - PMO Virtual.

## INFORMACIÓN DEL ESTUDIANTE
- Nombre: ${user.nombre}
- Nivel actual: ${user.nivelActual}
- Perfil profesional: ${user.perfilTipo}
- Módulos completados: ${user.modulosCompletados.join(', ') || 'Ninguno aún'}
- Módulo en curso: ${user.moduloActual || 'Ninguno'}

## NIVELES QUE PUEDE CONSULTAR
${content.nivelesPermitidos.map(n => `- ${n}`).join('\n')}

## REGLAS ESTRICTAS DE ASISTENCIA

1. **NUNCA** des información sobre niveles superiores al nivel ${user.nivelActual}
   - Si el estudiante pregunta sobre temas avanzados, responde:
     "Ese tema lo veremos en el Nivel X. Por ahora, enfoquémonos en dominar
     los conceptos de tu nivel actual. ¿Tienes alguna duda sobre [tema actual]?"

2. **SIEMPRE** refuerza el aprendizaje del nivel actual
   - Usa ejemplos relacionados con su perfil (${user.perfilTipo})
   - Conecta los conceptos con aplicaciones prácticas
   - Motiva a completar los módulos actuales

3. **SI** el estudiante está frustrado:
   - Ofrece una explicación alternativa
   - Sugiere revisar el material del módulo
   - Recomienda tomar un descanso si es necesario

4. **FORMATO DE RESPUESTAS**:
   - Respuestas concisas (máximo 200 palabras)
   - Usa viñetas para listas
   - Incluye emojis moderadamente para engagement
   - Si es código, usa bloques de código con syntax highlighting

## CONTENIDO DEL NIVEL ACTUAL
${content.contenidoNivelActual}

## CONTENIDO DEL MÓDULO ACTUAL
${content.moduloActual ? content.contenidoModuloActual : 'El estudiante no tiene un módulo en curso.'}

## TEMAS QUE NO DEBES ABORDAR (Niveles superiores)
- Nivel ${user.nivelActual + 1} en adelante está PROHIBIDO
- Si detectas que la pregunta es de nivel superior, redirige amablemente

Recuerda: Tu objetivo es que el estudiante DOMINE su nivel actual antes de avanzar.
`;
}
```

### 7.4 API Route del Asistente

```typescript
// app/api/asistente/route.ts

import { NextRequest, NextResponse } from 'next/server'
import Anthropic from '@anthropic-ai/sdk'
import { createServerSupabase } from '@/lib/supabase/server'
import { buildSystemPrompt } from '@/lib/claude/context-builder'
import { getContentForLevel, getContentForModule } from '@/lib/content'

const anthropic = new Anthropic({
  apiKey: process.env.ANTHROPIC_API_KEY!,
})

export async function POST(request: NextRequest) {
  try {
    const supabase = createServerSupabase()

    // Verificar autenticación
    const { data: { user } } = await supabase.auth.getUser()
    if (!user) {
      return NextResponse.json({ error: 'No autorizado' }, { status: 401 })
    }

    // Obtener datos del perfil
    const { data: perfil, error: perfilError } = await supabase
      .from('perfiles')
      .select('*')
      .eq('auth_id', user.id)
      .single()

    if (perfilError || !perfil) {
      return NextResponse.json({ error: 'Perfil no encontrado' }, { status: 404 })
    }

    // Verificar plan Premium
    if (perfil.plan !== 'premium' && perfil.plan !== 'enterprise') {
      return NextResponse.json({
        error: 'Esta función requiere plan Premium',
        upgrade_url: '/planes'
      }, { status: 403 })
    }

    // Obtener progreso del usuario
    const { data: progreso } = await supabase
      .from('progreso')
      .select('modulo_id, completado')
      .eq('user_id', perfil.id)

    const modulosCompletados = progreso
      ?.filter(p => p.completado)
      .map(p => p.modulo_id) || []

    // Obtener mensaje del usuario
    const body = await request.json()
    const { mensaje, moduloActual } = body

    if (!mensaje) {
      return NextResponse.json({ error: 'Mensaje requerido' }, { status: 400 })
    }

    // Obtener historial reciente de chat
    const { data: historial } = await supabase
      .from('chat_asistente')
      .select('mensaje, rol')
      .eq('user_id', perfil.id)
      .order('timestamp', { ascending: false })
      .limit(10)

    // Construir contexto
    const userContext = {
      userId: perfil.id,
      nombre: perfil.nombre || 'Estudiante',
      nivelActual: perfil.nivel_actual,
      perfilTipo: perfil.perfil_tipo,
      modulosCompletados,
      moduloActual,
    }

    // Obtener contenido permitido
    const nivelesPermitidos = []
    for (let i = 0; i <= perfil.nivel_actual; i++) {
      nivelesPermitidos.push(`Nivel ${i}`)
    }

    const contentContext = {
      nivelesPermitidos,
      contenidoNivelActual: await getContentForLevel(perfil.nivel_actual),
      contenidoModuloActual: moduloActual
        ? await getContentForModule(moduloActual)
        : '',
    }

    // Construir mensajes para Claude
    const messages: Anthropic.MessageParam[] = []

    // Agregar historial (invertido para orden cronológico)
    if (historial && historial.length > 0) {
      historial.reverse().forEach(h => {
        messages.push({
          role: h.rol === 'user' ? 'user' : 'assistant',
          content: h.mensaje,
        })
      })
    }

    // Agregar mensaje actual
    messages.push({
      role: 'user',
      content: mensaje,
    })

    // Llamar a Claude API
    const response = await anthropic.messages.create({
      model: 'claude-3-5-sonnet-20241022',
      max_tokens: 1024,
      system: buildSystemPrompt(userContext, contentContext),
      messages,
    })

    const respuestaIA = response.content[0].type === 'text'
      ? response.content[0].text
      : ''

    // Guardar en historial
    await supabase.from('chat_asistente').insert([
      {
        user_id: perfil.id,
        mensaje: mensaje,
        rol: 'user',
        contexto: { nivel: perfil.nivel_actual, modulo: moduloActual },
        tokens_usados: response.usage.input_tokens,
      },
      {
        user_id: perfil.id,
        mensaje: respuestaIA,
        rol: 'assistant',
        contexto: { nivel: perfil.nivel_actual, modulo: moduloActual },
        tokens_usados: response.usage.output_tokens,
      },
    ])

    return NextResponse.json({
      respuesta: respuestaIA,
      tokens_usados: response.usage.input_tokens + response.usage.output_tokens,
    })

  } catch (error: any) {
    console.error('Error en asistente:', error)
    return NextResponse.json(
      { error: 'Error interno del servidor' },
      { status: 500 }
    )
  }
}
```

### 7.5 Componente de Chat

```typescript
// components/features/ChatAsistente.tsx

'use client'

import { useState, useRef, useEffect } from 'react'
import { Send, Bot, User, Loader2, Lock } from 'lucide-react'

interface Message {
  id: string
  content: string
  role: 'user' | 'assistant'
  timestamp: Date
}

interface ChatAsistenteProps {
  moduloActual?: string
  isPremium: boolean
}

export default function ChatAsistente({ moduloActual, isPremium }: ChatAsistenteProps) {
  const [messages, setMessages] = useState<Message[]>([])
  const [input, setInput] = useState('')
  const [loading, setLoading] = useState(false)
  const messagesEndRef = useRef<HTMLDivElement>(null)

  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' })
  }

  useEffect(() => {
    scrollToBottom()
  }, [messages])

  // Mensaje de bienvenida
  useEffect(() => {
    setMessages([{
      id: 'welcome',
      content: '¡Hola! Soy PAIDEIA Assistant, tu tutor de IA. 🎓\n\nEstoy aquí para ayudarte con dudas sobre tu nivel actual. ¿En qué puedo asistirte hoy?',
      role: 'assistant',
      timestamp: new Date(),
    }])
  }, [])

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault()
    if (!input.trim() || loading) return

    const userMessage: Message = {
      id: Date.now().toString(),
      content: input.trim(),
      role: 'user',
      timestamp: new Date(),
    }

    setMessages(prev => [...prev, userMessage])
    setInput('')
    setLoading(true)

    try {
      const response = await fetch('/api/asistente', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          mensaje: userMessage.content,
          moduloActual,
        }),
      })

      const data = await response.json()

      if (!response.ok) {
        throw new Error(data.error || 'Error al obtener respuesta')
      }

      const assistantMessage: Message = {
        id: (Date.now() + 1).toString(),
        content: data.respuesta,
        role: 'assistant',
        timestamp: new Date(),
      }

      setMessages(prev => [...prev, assistantMessage])

    } catch (error: any) {
      const errorMessage: Message = {
        id: (Date.now() + 1).toString(),
        content: `Lo siento, hubo un error: ${error.message}`,
        role: 'assistant',
        timestamp: new Date(),
      }
      setMessages(prev => [...prev, errorMessage])
    } finally {
      setLoading(false)
    }
  }

  // Si no es Premium, mostrar mensaje de upgrade
  if (!isPremium) {
    return (
      <div className="flex flex-col items-center justify-center h-96 bg-gray-50 rounded-xl p-8">
        <Lock className="w-16 h-16 text-gray-400 mb-4" />
        <h3 className="text-xl font-semibold text-gray-700 mb-2">
          IA Asistente Premium
        </h3>
        <p className="text-gray-500 text-center mb-6 max-w-md">
          Obtén acceso a tu tutor de IA personal que te ayuda con dudas,
          refuerza tu aprendizaje y te guía en cada módulo.
        </p>
        <a
          href="/planes"
          className="px-6 py-3 bg-gradient-to-r from-purple-600 to-blue-600 text-white rounded-lg font-medium hover:opacity-90 transition"
        >
          Desbloquear Premium
        </a>
      </div>
    )
  }

  return (
    <div className="flex flex-col h-[600px] bg-white rounded-xl shadow-lg overflow-hidden">
      {/* Header */}
      <div className="px-4 py-3 bg-gradient-to-r from-purple-600 to-blue-600 text-white">
        <div className="flex items-center gap-3">
          <div className="w-10 h-10 bg-white/20 rounded-full flex items-center justify-center">
            <Bot className="w-6 h-6" />
          </div>
          <div>
            <h3 className="font-semibold">PAIDEIA Assistant</h3>
            <p className="text-xs text-white/80">Tu tutor de IA personal</p>
          </div>
        </div>
      </div>

      {/* Messages */}
      <div className="flex-1 overflow-y-auto p-4 space-y-4">
        {messages.map((message) => (
          <div
            key={message.id}
            className={`flex gap-3 ${
              message.role === 'user' ? 'flex-row-reverse' : ''
            }`}
          >
            <div
              className={`w-8 h-8 rounded-full flex items-center justify-center flex-shrink-0 ${
                message.role === 'user'
                  ? 'bg-blue-600 text-white'
                  : 'bg-purple-100 text-purple-600'
              }`}
            >
              {message.role === 'user' ? (
                <User className="w-5 h-5" />
              ) : (
                <Bot className="w-5 h-5" />
              )}
            </div>
            <div
              className={`max-w-[80%] rounded-2xl px-4 py-2 ${
                message.role === 'user'
                  ? 'bg-blue-600 text-white rounded-tr-none'
                  : 'bg-gray-100 text-gray-800 rounded-tl-none'
              }`}
            >
              <p className="whitespace-pre-wrap">{message.content}</p>
              <span
                className={`text-xs mt-1 block ${
                  message.role === 'user' ? 'text-blue-200' : 'text-gray-400'
                }`}
              >
                {message.timestamp.toLocaleTimeString([], {
                  hour: '2-digit',
                  minute: '2-digit',
                })}
              </span>
            </div>
          </div>
        ))}

        {loading && (
          <div className="flex gap-3">
            <div className="w-8 h-8 rounded-full bg-purple-100 flex items-center justify-center">
              <Bot className="w-5 h-5 text-purple-600" />
            </div>
            <div className="bg-gray-100 rounded-2xl rounded-tl-none px-4 py-3">
              <Loader2 className="w-5 h-5 animate-spin text-purple-600" />
            </div>
          </div>
        )}

        <div ref={messagesEndRef} />
      </div>

      {/* Input */}
      <form onSubmit={handleSubmit} className="p-4 border-t">
        <div className="flex gap-2">
          <input
            type="text"
            value={input}
            onChange={(e) => setInput(e.target.value)}
            placeholder="Escribe tu pregunta..."
            className="flex-1 px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-purple-500"
            disabled={loading}
          />
          <button
            type="submit"
            disabled={loading || !input.trim()}
            className="px-4 py-2 bg-purple-600 text-white rounded-lg hover:bg-purple-700 disabled:opacity-50 disabled:cursor-not-allowed transition"
          >
            <Send className="w-5 h-5" />
          </button>
        </div>
        <p className="text-xs text-gray-400 mt-2 text-center">
          El asistente solo puede ayudarte con temas de tu nivel actual
        </p>
      </form>
    </div>
  )
}
```

### 7.6 Ejemplos de Interacción

```
┌─────────────────────────────────────────────────────────────────┐
│                 EJEMPLOS DE INTERACCIÓN                          │
└─────────────────────────────────────────────────────────────────┘

CASO 1: Pregunta dentro del nivel (Nivel 1)
──────────────────────────────────────────
Usuario (Nivel 1): "¿Qué es un Project Manager?"

IA: "¡Excelente pregunta! 🎯

Un Project Manager (PM) es el profesional responsable de:
• Planificar el proyecto desde inicio a fin
• Coordinar al equipo de trabajo
• Gestionar recursos y presupuesto
• Asegurar que se cumplan los objetivos

En tu perfil de Empresario, piensa en el PM como el
'director de orquesta' de tus proyectos de negocio.

¿Te gustaría que profundicemos en alguna de estas
responsabilidades?"


CASO 2: Pregunta de nivel superior (Nivel 1 pregunta Nivel 3)
──────────────────────────────────────────────────────────────
Usuario (Nivel 1): "¿Cómo uso Claude para crear un PMO?"

IA: "Entiendo tu entusiasmo por aprender sobre PMO e IA! 🚀

Sin embargo, ese tema lo cubriremos en el **Nivel 3: PMO + IA**.

Por ahora, es importante que domines los fundamentos de
gestión de proyectos en tu nivel actual. Esto te dará
una base sólida para cuando lleguemos a integrar IA.

¿Tienes alguna duda sobre los conceptos del Nivel 1 que
estamos viendo? Por ejemplo:
• Ciclo de vida del proyecto
• Roles en un equipo de proyecto
• Herramientas básicas de PM

¡Vamos paso a paso! 💪"


CASO 3: Pregunta práctica del nivel actual
──────────────────────────────────────────
Usuario (Nivel 2): "No entiendo cómo hacer un buen prompt"

IA: "¡El prompt engineering es una habilidad clave! 📝

Aquí tienes la estructura básica de un buen prompt:

1. **Contexto**: Explica la situación
2. **Rol**: Define quién es la IA
3. **Tarea**: Qué necesitas que haga
4. **Formato**: Cómo quieres la respuesta

**Ejemplo para tu perfil de Contador**:
\`\`\`
Actúa como un experto fiscal.
Contexto: Tengo un cliente pequeño negocio.
Tarea: Crea una checklist de documentos para declaración.
Formato: Lista numerada con explicación breve.
\`\`\`

¿Quieres que practiquemos con un caso específico de tu área?"
```

---

## 8. SISTEMA DE PROGRESO Y CERTIFICADOS

### 8.1 Hook de Progreso

```typescript
// hooks/useProgreso.ts

import { useState, useEffect } from 'react'
import { createClient } from '@/lib/supabase/client'

interface Progreso {
  nivelActual: number
  porcentajeTotal: number
  modulosCompletados: string[]
  siguienteModulo: string | null
}

export function useProgreso() {
  const [progreso, setProgreso] = useState<Progreso | null>(null)
  const [loading, setLoading] = useState(true)
  const supabase = createClient()

  useEffect(() => {
    fetchProgreso()
  }, [])

  const fetchProgreso = async () => {
    try {
      const { data: { user } } = await supabase.auth.getUser()
      if (!user) return

      // Obtener perfil
      const { data: perfil } = await supabase
        .from('perfiles')
        .select('nivel_actual')
        .eq('auth_id', user.id)
        .single()

      // Obtener progreso
      const { data: progresoData } = await supabase
        .from('progreso')
        .select('*')
        .eq('user_id', perfil?.id)

      const modulosCompletados = progresoData
        ?.filter(p => p.completado)
        .map(p => p.modulo_id) || []

      // Calcular porcentaje (asumiendo 30 módulos totales)
      const totalModulos = 30
      const porcentajeTotal = Math.round((modulosCompletados.length / totalModulos) * 100)

      setProgreso({
        nivelActual: perfil?.nivel_actual || 0,
        porcentajeTotal,
        modulosCompletados,
        siguienteModulo: calcularSiguienteModulo(modulosCompletados),
      })
    } catch (error) {
      console.error('Error fetching progreso:', error)
    } finally {
      setLoading(false)
    }
  }

  const marcarCompletado = async (moduloId: string, nivelId: string) => {
    try {
      const { data: { user } } = await supabase.auth.getUser()
      if (!user) return

      const { data: perfil } = await supabase
        .from('perfiles')
        .select('id')
        .eq('auth_id', user.id)
        .single()

      await supabase
        .from('progreso')
        .upsert({
          user_id: perfil?.id,
          nivel_id: nivelId,
          modulo_id: moduloId,
          completado: true,
          fecha_completado: new Date().toISOString(),
        })

      // Refrescar progreso
      await fetchProgreso()

    } catch (error) {
      console.error('Error marcando completado:', error)
    }
  }

  return { progreso, loading, marcarCompletado, refetch: fetchProgreso }
}

function calcularSiguienteModulo(completados: string[]): string | null {
  const ordenModulos = [
    'modulo-0-1', 'modulo-1-1', 'modulo-1-2', 'modulo-1-3',
    'modulo-2-1', 'modulo-2-2', 'modulo-2-3',
    // ... etc
  ]

  for (const modulo of ordenModulos) {
    if (!completados.includes(modulo)) {
      return modulo
    }
  }
  return null
}
```

### 8.2 Generación de Certificados

```typescript
// app/api/certificado/route.ts

import { NextRequest, NextResponse } from 'next/server'
import { createServerSupabase } from '@/lib/supabase/server'
import { jsPDF } from 'jspdf'

export async function POST(request: NextRequest) {
  try {
    const supabase = createServerSupabase()
    const { data: { user } } = await supabase.auth.getUser()

    if (!user) {
      return NextResponse.json({ error: 'No autorizado' }, { status: 401 })
    }

    const body = await request.json()
    const { nivelId, tipoCertificado } = body

    // Obtener perfil
    const { data: perfil } = await supabase
      .from('perfiles')
      .select('*')
      .eq('auth_id', user.id)
      .single()

    if (!perfil) {
      return NextResponse.json({ error: 'Perfil no encontrado' }, { status: 404 })
    }

    // Verificar que el nivel está completado
    const { data: progreso } = await supabase
      .from('progreso')
      .select('*')
      .eq('user_id', perfil.id)
      .eq('nivel_id', nivelId)
      .eq('completado', true)

    const modulosPorNivel = {
      'nivel-0': 1,
      'nivel-1': 4,
      'nivel-2': 3,
      'nivel-3': 4,
      'nivel-4': 3,
    }

    if (!progreso || progreso.length < (modulosPorNivel[nivelId as keyof typeof modulosPorNivel] || 0)) {
      return NextResponse.json({
        error: 'Nivel no completado aún'
      }, { status: 400 })
    }

    // Generar código único
    const { data: codigoData } = await supabase.rpc('generar_codigo_verificacion')
    const codigoVerificacion = codigoData

    // Generar PDF
    const pdfBase64 = generarCertificadoPDF({
      nombre: perfil.nombre || 'Estudiante',
      nivel: nivelId,
      fecha: new Date().toLocaleDateString('es-ES'),
      codigo: codigoVerificacion,
    })

    // Guardar en storage
    const { data: uploadData, error: uploadError } = await supabase.storage
      .from('certificados')
      .upload(`${perfil.id}/${codigoVerificacion}.pdf`,
        Buffer.from(pdfBase64, 'base64'),
        { contentType: 'application/pdf' }
      )

    if (uploadError) throw uploadError

    // Obtener URL pública
    const { data: urlData } = supabase.storage
      .from('certificados')
      .getPublicUrl(`${perfil.id}/${codigoVerificacion}.pdf`)

    // Guardar registro en BD
    const { data: certificado, error: certError } = await supabase
      .from('certificados')
      .insert({
        user_id: perfil.id,
        tipo_certificado: tipoCertificado,
        nivel_id: nivelId,
        codigo_verificacion: codigoVerificacion,
        pdf_url: urlData.publicUrl,
        metadata: {
          nombre: perfil.nombre,
          perfil_tipo: perfil.perfil_tipo,
        }
      })
      .select()
      .single()

    if (certError) throw certError

    return NextResponse.json({
      certificado,
      pdf_url: urlData.publicUrl,
      codigo_verificacion: codigoVerificacion,
    })

  } catch (error: any) {
    console.error('Error generando certificado:', error)
    return NextResponse.json(
      { error: 'Error interno del servidor' },
      { status: 500 }
    )
  }
}

function generarCertificadoPDF(data: {
  nombre: string
  nivel: string
  fecha: string
  codigo: string
}): string {
  const doc = new jsPDF({
    orientation: 'landscape',
    unit: 'mm',
    format: 'a4',
  })

  // Fondo degradado (simplificado)
  doc.setFillColor(88, 28, 135) // purple-900
  doc.rect(0, 0, 297, 210, 'F')

  // Marco decorativo
  doc.setDrawColor(255, 255, 255)
  doc.setLineWidth(2)
  doc.rect(15, 15, 267, 180)
  doc.rect(20, 20, 257, 170)

  // Logo/Título
  doc.setTextColor(255, 255, 255)
  doc.setFontSize(24)
  doc.setFont('helvetica', 'bold')
  doc.text('PAIDEIA', 148.5, 45, { align: 'center' })

  doc.setFontSize(14)
  doc.setFont('helvetica', 'normal')
  doc.text('PMO Virtual - Formación en IA', 148.5, 55, { align: 'center' })

  // Certificado
  doc.setFontSize(36)
  doc.setFont('helvetica', 'bold')
  doc.text('CERTIFICADO', 148.5, 80, { align: 'center' })

  doc.setFontSize(14)
  doc.setFont('helvetica', 'normal')
  doc.text('Se certifica que', 148.5, 100, { align: 'center' })

  // Nombre
  doc.setFontSize(28)
  doc.setFont('helvetica', 'bold')
  doc.text(data.nombre.toUpperCase(), 148.5, 115, { align: 'center' })

  // Nivel completado
  const nivelNombre = {
    'nivel-0': 'Nivel 0: Despertar',
    'nivel-1': 'Nivel 1: Fundamentos PM',
    'nivel-2': 'Nivel 2: Herramientas IA',
    'nivel-3': 'Nivel 3: PMO + IA',
    'nivel-4': 'Nivel 4: Especialización',
    'nivel-5': 'MASTER PAIDEIA',
  }

  doc.setFontSize(14)
  doc.setFont('helvetica', 'normal')
  doc.text('ha completado satisfactoriamente el', 148.5, 130, { align: 'center' })

  doc.setFontSize(22)
  doc.setFont('helvetica', 'bold')
  doc.text(nivelNombre[data.nivel as keyof typeof nivelNombre] || data.nivel, 148.5, 145, { align: 'center' })

  // Fecha
  doc.setFontSize(12)
  doc.setFont('helvetica', 'normal')
  doc.text(`Fecha de emisión: ${data.fecha}`, 148.5, 165, { align: 'center' })

  // Código de verificación
  doc.setFontSize(10)
  doc.text(`Código de verificación: ${data.codigo}`, 148.5, 175, { align: 'center' })
  doc.text('Verificar en: paideia.com/verificar', 148.5, 182, { align: 'center' })

  return doc.output('datauristring').split(',')[1]
}
```

---

## 9. DEPLOYMENT Y CI/CD

### 9.1 Configuración Vercel

```javascript
// next.config.js
/** @type {import('next').NextConfig} */
const nextConfig = {
  images: {
    remotePatterns: [
      {
        protocol: 'https',
        hostname: '*.supabase.co',
      },
    ],
  },
  experimental: {
    serverActions: true,
  },
}

module.exports = nextConfig
```

### 9.2 Variables de Entorno

```bash
# .env.local (desarrollo)
# .env.production (producción en Vercel)

# Supabase
NEXT_PUBLIC_SUPABASE_URL=https://xxxxx.supabase.co
NEXT_PUBLIC_SUPABASE_ANON_KEY=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
SUPABASE_SERVICE_ROLE_KEY=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...

# Claude API
ANTHROPIC_API_KEY=sk-ant-api03-...

# App
NEXT_PUBLIC_APP_URL=https://paideia.com
```

### 9.3 Flujo de Deploy

```
┌─────────────────────────────────────────────────────────────────┐
│                    FLUJO CI/CD                                   │
└─────────────────────────────────────────────────────────────────┘

      [Desarrollador]
            │
            │ git push origin main
            ▼
      ┌───────────┐
      │  GitHub   │
      │   Repo    │
      └─────┬─────┘
            │ Webhook automático
            ▼
      ┌───────────┐
      │  Vercel   │
      │  Build    │
      └─────┬─────┘
            │
    ┌───────┼───────┐
    ▼       ▼       ▼
[Lint]  [Types] [Build]
    │       │       │
    └───────┼───────┘
            │
            ▼ (si todo pasa)
      ┌───────────┐
      │  Deploy   │
      │ Preview   │
      └─────┬─────┘
            │ (merge a main)
            ▼
      ┌───────────┐
      │Production │
      │  Deploy   │
      └───────────┘
```

---

## 10. COSTOS Y ESCALABILIDAD

### 10.1 Tabla de Costos

```
┌─────────────────────────────────────────────────────────────────┐
│                    COSTOS ESTIMADOS                              │
└─────────────────────────────────────────────────────────────────┘

TIER GRATUITO (Desarrollo + MVP)
────────────────────────────────
Supabase Free:
  • 500 MB database
  • 1 GB storage
  • 2 GB bandwidth
  • 50,000 auth users
  → $0/mes

Vercel Hobby:
  • 100 GB bandwidth
  • Unlimited deploys
  • Serverless functions
  → $0/mes

Claude API (desarrollo):
  • Pay-as-you-go
  • ~$3/1M input tokens
  • ~$15/1M output tokens
  → ~$10-20/mes (desarrollo)

TOTAL DESARROLLO: ~$10-20/mes


TIER PRODUCCIÓN (1,000+ usuarios)
──────────────────────────────────
Supabase Pro:
  • 8 GB database
  • 100 GB storage
  • Backups diarios
  → $25/mes

Vercel Pro:
  • Unlimited bandwidth
  • Analytics
  • Team features
  → $20/mes

Claude API (producción):
  • Estimado 10,000 mensajes/mes
  • ~$50-100/mes

TOTAL PRODUCCIÓN: ~$100-150/mes


TIER ESCALA (10,000+ usuarios)
──────────────────────────────
Supabase Team: $599/mes
Vercel Enterprise: Personalizado
Claude API: $500+/mes

TOTAL ESCALA: $1,000-2,000/mes
```

### 10.2 Estrategia de Escalabilidad

```
┌─────────────────────────────────────────────────────────────────┐
│                    ESCALABILIDAD                                 │
└─────────────────────────────────────────────────────────────────┘

FASE 1: MVP (0-100 usuarios)
• Supabase Free + Vercel Hobby
• Costo: $0-20/mes
• Foco: Validar producto

FASE 2: Crecimiento (100-1,000 usuarios)
• Supabase Pro + Vercel Pro
• Costo: $100-200/mes
• Foco: Retención y conversión

FASE 3: Escala (1,000-10,000 usuarios)
• Supabase Team
• Vercel Enterprise
• Costo: $500-2,000/mes
• Foco: Monetización Premium

OPTIMIZACIONES:
• Caché de contenido (Redis)
• CDN para assets
• Rate limiting en API de IA
• Limitar tokens por usuario/día
```

---

## 11. SPRINTS DE IMPLEMENTACIÓN

### Sprint 0: Setup Inicial (1-2 días)
```
□ Crear proyecto Next.js con TypeScript
□ Configurar Tailwind CSS
□ Crear proyecto Supabase
□ Configurar variables de entorno
□ Deploy inicial a Vercel
□ Conectar GitHub → Vercel
```

### Sprint 1: Autenticación (2-3 días)
```
□ Implementar páginas login/registro
□ Configurar Supabase Auth
□ Agregar OAuth (Google)
□ Crear middleware de protección
□ Implementar logout
```

### Sprint 2: Base de Datos (2-3 días)
```
□ Crear migraciones SQL
□ Configurar Row Level Security
□ Implementar funciones/triggers
□ Crear tipos TypeScript generados
□ Testear conexión desde app
```

### Sprint 3: Dashboard y Progreso (3-4 días)
```
□ Diseñar layout principal
□ Implementar sidebar navegación
□ Crear componentes de progreso
□ Implementar hook useProgreso
□ Mostrar módulos desbloqueados
```

### Sprint 4: Contenido y Módulos (4-5 días)
```
□ Migrar contenido a MDX
□ Crear páginas de nivel/módulo
□ Implementar sistema de videos
□ Crear quizzes de evaluación
□ Sistema de marcado completado
```

### Sprint 5: Quiz de Perfil (2-3 días)
```
□ Diseñar quiz interactivo
□ Implementar lógica de scoring
□ Guardar resultado en BD
□ Asignar ruta personalizada
□ Mostrar recomendaciones
```

### Sprint 6: IA Asistente (3-4 días)
```
□ Configurar Claude API
□ Implementar context builder
□ Crear API route /api/asistente
□ Diseñar componente ChatAsistente
□ Implementar restricción por nivel
□ Guardar historial de chat
```

### Sprint 7: Certificados (2-3 días)
```
□ Diseñar template PDF
□ Implementar generación con jsPDF
□ Crear API route /api/certificado
□ Subir a Supabase Storage
□ Página de verificación pública
```

### Sprint 8: Premium y Pagos (3-4 días)
```
□ Integrar Stripe
□ Crear planes de suscripción
□ Implementar webhooks
□ Actualizar permisos por plan
□ Página de precios
```

### Sprint 9: Testing y QA (2-3 días)
```
□ Tests unitarios críticos
□ Tests de integración auth
□ Test de flujo completo
□ Pruebas de carga básicas
□ Corrección de bugs
```

### Sprint 10: Launch Prep (2-3 días)
```
□ SEO y meta tags
□ Analytics (Vercel + custom)
□ Monitoreo de errores (Sentry)
□ Documentación usuario
□ Soft launch con beta testers
```

---

## 📎 ANEXOS

### A. Comandos Útiles

```bash
# Desarrollo local
npm run dev                    # Iniciar servidor desarrollo
npm run build                  # Build producción
npm run lint                   # Verificar código

# Supabase
npx supabase start            # Iniciar Supabase local
npx supabase db push          # Aplicar migraciones
npx supabase gen types ts     # Generar tipos TypeScript

# Deployment
vercel                        # Deploy preview
vercel --prod                 # Deploy producción
```

### B. Enlaces de Referencia

- **Next.js Docs**: https://nextjs.org/docs
- **Supabase Docs**: https://supabase.com/docs
- **Claude API**: https://docs.anthropic.com
- **Vercel Docs**: https://vercel.com/docs
- **Tailwind CSS**: https://tailwindcss.com/docs

---

**Documento creado**: 29 de Noviembre 2025
**Última actualización**: 29 de Noviembre 2025
**Versión**: 1.0
**Estado**: ✅ Aprobado para implementación
