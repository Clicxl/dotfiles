export type headersType = {
  "Content-Type"?: string;
  "Authorization"?: string;
};

export interface formConfigType extends RequestInit {
  method: "POST" | "GET";
  headers: headersType;
  credentials: RequestCredentials;
  body?: string;
}
