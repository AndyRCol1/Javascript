import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

import { Product, CreateProductDTO, UpdateProductDTO } from './../models/product.model';

@Injectable({
  providedIn: 'root'
})
export class ProductsService {
  private apiUrl = 'https://young-sands-07814.herokuapp.com/api/products'

  constructor(
    private http: HttpClient
  ) { }

  getAllProducts() {
    return this.http.get<Product[]>(this.apiUrl);
  }

  getProducts(id: string){
    return this.http.get<Product>(`${this.apiUrl}/${id}`);
  }

  getProductBYPage(limit: number, offset: number){
    return this.http.get<Product[]>(`${this.apiUrl}`, {
      params: { limit, offset}
    })
  }

  create(data: CreateProductDTO) {
    return this.http.post<Product>(this.apiUrl, data);
  }

  update(id: string, data: UpdateProductDTO) {
    return this.http.put<Product>(`${this.apiUrl}/${id}`, data);
  }

  delete(id: string){
    return this.http.delete<boolean>(`${this.apiUrl}/${id}`);
  }
}
