import { CollectionConfig } from 'payload/types';

const Coaches: CollectionConfig = {
  slug: 'coaches',
  admin: {
    useAsTitle: 'name',
  },
  access: {
    read: () => true, // Public pour l'affichage
  },
  fields: [
    {
      name: 'name',
      type: 'text',
      required: true,
    },
    {
      name: 'specialty',
      type: 'select',
      options: [
        { label: 'Coaching de vie', value: 'life' },
        { label: 'Coaching professionnel', value: 'career' },
        { label: 'Coaching sportif', value: 'fitness' },
        { label: 'Coaching mental', value: 'mental' },
      ],
      required: true,
    },
    {
      name: 'bio',
      type: 'richText',
    },
    {
      name: 'avatar',
      type: 'upload',
      relationTo: 'media',
    },
    {
      name: 'hourlyRate',
      type: 'number',
      required: true,
      min: 0,
    },
    {
      name: 'rating',
      type: 'number',
      min: 0,
      max: 5,
      defaultValue: 5,
    },
    {
      name: 'availability',
      type: 'json',
      admin: {
        description: 'Planning de disponibilité JSON',
      },
    },
    {
      name: 'userId',
      type: 'relationship',
      relationTo: 'users',
      required: true,
    },
  ],
};

export default Coaches;
