import { CollectionConfig } from 'payload/types';

const Appointments: CollectionConfig = {
  slug: 'appointments',
  admin: {
    useAsTitle: 'title',
  },
  fields: [
    {
      name: 'title',
      type: 'text',
      required: true,
    },
    {
      name: 'coach',
      type: 'relationship',
      relationTo: 'coaches',
      required: true,
    },
    {
      name: 'client',
      type: 'relationship',
      relationTo: 'users',
      required: true,
    },
    {
      name: 'scheduledAt',
      type: 'date',
      required: true,
      admin: {
        date: {
          pickerAppearance: 'dayAndTime',
        },
      },
    },
    {
      name: 'duration',
      type: 'number',
      defaultValue: 60,
      admin: {
        description: 'Durée en minutes',
      },
    },
    {
      name: 'status',
      type: 'select',
      options: [
        { label: 'Programmé', value: 'scheduled' },
        { label: 'Confirmé', value: 'confirmed' },
        { label: 'En cours', value: 'in-progress' },
        { label: 'Terminé', value: 'completed' },
        { label: 'Annulé', value: 'cancelled' },
      ],
      defaultValue: 'scheduled',
    },
    {
      name: 'meetingUrl',
      type: 'text',
      admin: {
        description: 'URL de la visioconférence LiveKit',
      },
    },
    {
      name: 'notes',
      type: 'textarea',
    },
  ],
};

export default Appointments;
