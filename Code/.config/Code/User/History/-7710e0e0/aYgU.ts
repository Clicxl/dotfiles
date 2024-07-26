export type headersType = {"Content-Type": string}

export interface formConfigType extends PromiseIni{
  method: "POST";
  headers: headersType;
  credentials: string;
  body: string;
};
