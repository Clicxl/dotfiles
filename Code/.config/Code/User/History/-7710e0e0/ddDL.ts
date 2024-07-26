export type headersType = {"Content-Type": string}

export type formConfigType = {
  method: "POST";
  headers: headersType;
  credentials: string;
};
