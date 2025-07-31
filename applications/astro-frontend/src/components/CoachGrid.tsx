import React, { useState, useEffect } from 'react';

interface Coach {
  id: string;
  name: string;
  specialty: string;
  avatar: string;
  rating: number;
  hourlyRate: number;
}

export default function CoachGrid() {
  const [coaches, setCoaches] = useState<Coach[]>([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetchCoaches();
  }, []);

  const fetchCoaches = async () => {
    try {
      const response = await fetch(`${import.meta.env.PAYLOAD_API_URL}/api/coaches`);
      const data = await response.json();
      setCoaches(data.docs);
    } catch (error) {
      console.error('Erreur lors du chargement des coaches:', error);
    } finally {
      setLoading(false);
    }
  };

  if (loading) {
    return (
      <div className="max-w-7xl mx-auto px-4 py-16">
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
          {[...Array(6)].map((_, i) => (
            <div key={i} className="animate-pulse">
              <div className="bg-gray-300 h-48 rounded-lg mb-4"></div>
              <div className="bg-gray-300 h-4 rounded mb-2"></div>
              <div className="bg-gray-300 h-4 rounded w-3/4"></div>
            </div>
          ))}
        </div>
      </div>
    );
  }

  return (
    <section className="max-w-7xl mx-auto px-4 py-16">
      <h2 className="text-3xl font-bold text-center mb-12">Nos coaches experts</h2>
      
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        {coaches.map((coach) => (
          <div key={coach.id} className="bg-white rounded-lg shadow-md overflow-hidden hover:shadow-lg transition-shadow">
            <img 
              src={coach.avatar || '/default-avatar.jpg'} 
              alt={coach.name}
              className="w-full h-48 object-cover"
            />
            <div className="p-6">
              <h3 className="text-xl font-semibold mb-2">{coach.name}</h3>
              <p className="text-gray-600 mb-3">{coach.specialty}</p>
              <div className="flex justify-between items-center">
                <div className="flex items-center">
                  <span className="text-yellow-500">★</span>
                  <span className="ml-1 text-sm text-gray-600">{coach.rating}/5</span>
                </div>
                <span className="text-lg font-bold text-blue-600">{coach.hourlyRate}€/h</span>
              </div>
              <button className="w-full mt-4 bg-blue-600 text-white py-2 rounded-md hover:bg-blue-700">
                Réserver une séance
              </button>
            </div>
          </div>
        ))}
      </div>
    </section>
  );
}
