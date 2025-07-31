import { defineConfig } from "tinacms";

export default defineConfig({
  branch: "main",
  clientId: process.env.TINA_CLIENT_ID!,
  token: process.env.TINA_TOKEN!,
  
  build: {
    outputFolder: "admin",
    publicFolder: "public",
  },
  
  media: {
    tina: {
      mediaRoot: "uploads",
      publicFolder: "public",
    },
  },
  
  schema: {
    collections: [
      {
        name: "page",
        label: "Pages",
        path: "content/pages",
        fields: [
          {
            type: "string",
            name: "title",
            label: "Title",
            isTitle: true,
            required: true,
          },
          {
            type: "rich-text",
            name: "body",
            label: "Body",
            isBody: true,
          },
          {
            type: "object",
            name: "seo",
            label: "SEO",
            fields: [
              {
                type: "string",
                name: "title",
                label: "SEO Title",
              },
              {
                type: "string",
                name: "description",
                label: "SEO Description",
              },
            ],
          },
        ],
      },
      {
        name: "coach",
        label: "Coaches",
        path: "content/coaches",
        fields: [
          {
            type: "string",
            name: "name",
            label: "Name",
            required: true,
          },
          {
            type: "string",
            name: "specialty",
            label: "Specialty",
          },
          {
            type: "image",
            name: "avatar",
            label: "Avatar",
          },
          {
            type: "rich-text",
            name: "bio",
            label: "Biography",
          },
          {
            type: "number",
            name: "hourlyRate",
            label: "Hourly Rate (€)",
          },
        ],
      },
    ],
  },
});
