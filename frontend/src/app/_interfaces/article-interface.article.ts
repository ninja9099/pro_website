import { IUser } from './user-interface';

export interface Itags {
    id: number;
    name: string;
    resource_uri: string;
    slug: string;
    tags: string;
}

export interface IArticle {
    article_content: string;
    article_image: string;
    article_state: string;
    article_tags: Itags[];
    article_title: string;
    author: IUser;
    comments: string;
    created: string;
    follow_list: any[];
    id: number;
    likes: any[];
    modified: string;
    resource_uri: string;
    slug: string;
    total_rating: number;
    total_reads: number;
}


export class CArticle {

    article_content: string;
    article_image: object;
    article_tags: any;
    article_title: string;
    article_category: any;
    article_subcategory: any;
    article_author: number;

    constructor(values: Object = {}) {
        // Constructor initialization
        Object.assign(this, values);
    }

}
