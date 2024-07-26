export type headersType = {"Content-Type": string}

export interface formConfigType extends RequestInit {
  method: "POST";
  headers: headersType;
  credentials: RequestCredentials;
  body: string;
};
