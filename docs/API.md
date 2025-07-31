# API Reference CoachLibre

## Endpoints Principaux

### Authentification
```
POST /api/auth/login
POST /api/auth/register
POST /api/auth/logout
```

### Coaches
```
GET /api/coaches
GET /api/coaches/:id
POST /api/coaches (auth required)
PUT /api/coaches/:id (auth required)
```

### Rendez-vous
```
GET /api/appointments
POST /api/appointments (auth required)
PUT /api/appointments/:id (auth required)
DELETE /api/appointments/:id (auth required)
```

### IA Assistant
```
POST /api/ai/chat
POST /api/ai/diagnose
POST /api/ai/recommend-coach
```

## Webhooks

### n8n Workflows
```
POST /webhook/appointment-reminder
POST /webhook/payment-processed
POST /webhook/coach-available
```

### Intégrations
```
POST /webhook/calendar/google
POST /webhook/payment/stripe
POST /webhook/video/livekit
```
