import axios from 'axios';

const API_Base = 'http://localhost:8000/api';

export interface TripRequest {
    destination: string;
    start_location: string;
    days: number;
    budget: string;
    style: string;
}

export interface TripResponse {
    result: Array<{
        agent: string;
        content: string;
    }>;
}

export const planTrip = async (data: TripRequest): Promise<TripResponse> => {
    const response = await axios.post<TripResponse>(`${API_Base}/plan-trip`, data);
    return response.data;
};
