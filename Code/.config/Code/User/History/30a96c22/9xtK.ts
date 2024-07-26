export interface modResponseType {
  author: string;
  categories: string[];
  client_side: string;
  color: number;
  date_created: string;
  date_modified: string;
  description: string;
  display_categories: string[];
  downloads: number;
  featured_gallery: any;
  follows: number;
  gallery: string[];
  icon_url: string;
  latest_version: string;
  license: string;
  project_id: string;
  project_type: string;
  server_side: string;
  slug: string;
  title: string;
  versions: string[];
};

export interface modType<object> {
  author: string;
  categories: string[];
  client_side: string;
  description: string;
  downloads: number;
  icon_url: string;
  latest_version: string;
  project_id: string;
  prohect_type: string;
  slug: string;
  title: string;
  versions: string[];
}
