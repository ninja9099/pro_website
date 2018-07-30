export interface IUser {
    article_reads: number;
    articles_authored: string[];
    bio: string;
    birth_date: string;
    comments: any[];
    date_joined: string;
    first_name: string;
    full_name: string;
    id: number;
    last_login: string;
    last_name: string;
    location: string;
    profile_picture: string;
    resource_uri: string;
    username: string;
}

export interface IResponse {
    meta: Object;
    objects: any[];
}
