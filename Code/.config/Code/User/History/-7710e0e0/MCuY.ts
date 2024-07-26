export type headersType = {"Content-Type": string}

export interface formConfigType extends Promise{
  method: "POST";
  headers: headersType;
  credentials: string;
  body: string;
};
