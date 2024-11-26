create database escritorio;

create table arquiteto(
    id int(5),
    nome int(5),
    CPF int(11),
    RG int(9),
    telefone int(11),
    email varchar(45),
    cidade varchar(45),
    estado varchar(45),
    endereco varchar(45),
    primary key(id));

create table cliente(
    id int(5),
    nome int(5),
    CPF int(11),
    RG int(9),
    telefone int(11),
    email varchar(45),
    cidade varchar(45),
    estado varchar(45),
    endereco varchar(45),
    primary key(id));

create table projeto(
    id int(5),
    projeto varchar(45),
    tipo varchar(45),
    orcamento float(10,2),
    data_inicio date,
    data_entrega date,
    id_cliente int(5),
    id_arquiteto int(5),
    primary key(id),
    foreign key(id_cliente) references cliente(id),
    foreign key(id_arquiteto) references arquiteto(id));