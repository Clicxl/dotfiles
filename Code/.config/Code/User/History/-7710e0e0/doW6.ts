export type headersType = {"Content-Type": string}

export interface formConfigType extends RequestInit{
  method: "POST";
  headers: headersType;
  credentials: string;
  body: string;
};
