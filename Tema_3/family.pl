:- discontiguous es_hijo_de/2.
:- discontiguous es_padre_de/2.
:- discontiguous es_madre_de/2.
:- discontiguous hermano_de/2.
:- discontiguous primo_de/2.

% Yo
es_hijo_de(alejandro, ana_lilia).
es_hijo_de(alejandro, alejandro).

% Hermanos
es_hijo_de(jazmin, ana_lilia).
es_hijo_de(jazmin, alejandro).

% Padres
es_padre_de(alejandro, jazmin).
es_padre_de(alejandro, alejandro).
es_madre_de(ana_lilia, jazmin).
es_madre_de(ana_lilia, alejandro).

% Tíos paternos
es_hijo_de(josefina, ruperto).
es_hijo_de(josefina, margarita).
es_hijo_de(nicolas, ruperto).
es_hijo_de(nicolas, margarita).
es_hijo_de(martina, ruperto).
es_hijo_de(martina, margarita).
es_hijo_de(maria, ruperto).
es_hijo_de(maria, margarita).
es_hijo_de(juan, ruperto).
es_hijo_de(juan, margarita).
es_hijo_de(david, ruperto).
es_hijo_de(david, margarita).
es_hijo_de(carmela, ruperto).
es_hijo_de(carmela, margarita).

% Tíos maternos
es_hijo_de(erick, fernando).
es_hijo_de(erick, mariana).
es_hijo_de(luis, fernando).
es_hijo_de(luis, mariana).
es_hijo_de(luis_fernando, fernando).
es_hijo_de(luis_fernando, mariana).
es_hijo_de(sonia, fernando).
es_hijo_de(sonia, mariana).
es_hijo_de(erick, fernando).
es_hijo_de(erick, mariana).
es_hijo_de(miguel, fernando).
es_hijo_de(miguel, mariana).
es_hijo_de(patricia, fernando).
es_hijo_de(patricia, mariana).

% Abuelos
es_hijo_de(margarita, ruperto).
es_hijo_de(ruperto, _).
es_hijo_de(fernando, _).
es_hijo_de(mariana, _).

% Primos (hijos de los tíos)
es_hijo_de(esmeralda, josefina).
es_hijo_de(paloma, josefina).
es_hijo_de(octavio, juan).
es_hijo_de(arturo, maria).
es_hijo_de(sebastian, maria).
es_hijo_de(mariana, miguel).
es_hijo_de(tatiana, patricia).
es_hijo_de(cynthia, patricia).

% Relaciones de padres
es_padre_de(alejandro, jazmin).
es_padre_de(alejandro, alejandro).
es_madre_de(ana_lilia, jazmin).
es_madre_de(ana_lilia, alejandro).
es_padre_de(josefina, esmeralda).
es_padre_de(josefina, paloma).
es_padre_de(juan, octavio).
es_padre_de(maria, arturo).
es_padre_de(maria, sebastian).
es_padre_de(miguel, mariana).
es_padre_de(patricia, tatiana).
es_padre_de(patricia, cynthia).

% Relaciones de hermanos
hermano_de(jazmin, alejandro).
hermano_de(alejandro, jazmin).

hermano_de(josefina, nicolas).
hermano_de(josefina, martina).
hermano_de(josefina, maria).
hermano_de(josefina, juan).
hermano_de(josefina, david).
hermano_de(josefina, carmela).

hermano_de(nicolas, josefina).
hermano_de(nicolas, martina).
hermano_de(nicolas, maria).
hermano_de(nicolas, juan).
hermano_de(nicolas, david).
hermano_de(nicolas, carmela).

hermano_de(martina, josefina).
hermano_de(martina, nicolas).
hermano_de(martina, maria).
hermano_de(martina, juan).
hermano_de(martina, david).
hermano_de(martina, carmela).

hermano_de(maria, josefina).
hermano_de(maria, nicolas).
hermano_de(maria, martina).
hermano_de(maria, juan).
hermano_de(maria, david).
hermano_de(maria, carmela).

hermano_de(juan, josefina).
hermano_de(juan, nicolas).
hermano_de(juan, martina).
hermano_de(juan, maria).
hermano_de(juan, david).
hermano_de(juan, carmela).

hermano_de(david, josefina).
hermano_de(david, nicolas).
hermano_de(david, martina).
hermano_de(david, maria).
hermano_de(david, juan).
hermano_de(david, carmela).

hermano_de(carmela, josefina).
hermano_de(carmela, nicolas).
hermano_de(carmela, martina).
hermano_de(carmela, maria).
hermano_de(carmela, juan).
hermano_de(carmela, david).

% Tíos maternos
hermano_de(erick, luis).
hermano_de(erick, luis_fernando).
hermano_de(erick, sonia).
hermano_de(erick, miguel).
hermano_de(erick, patricia).

hermano_de(luis, erick).
hermano_de(luis, luis_fernando).
hermano_de(luis, sonia).
hermano_de(luis, erick).
hermano_de(luis, miguel).
hermano_de(luis, patricia).

hermano_de(luis_fernando, erick).
hermano_de(luis_fernando, luis).
hermano_de(luis_fernando, sonia).
hermano_de(luis_fernando, erick).
hermano_de(luis_fernando, miguel).
hermano_de(luis_fernando, patricia).

hermano_de(sonia, erick).
hermano_de(sonia, luis).
hermano_de(sonia, luis_fernando).
hermano_de(sonia, erick).
hermano_de(sonia, miguel).
hermano_de(sonia, patricia).

hermano_de(erick, erick).
hermano_de(erick, luis).
hermano_de(erick, luis_fernando).
hermano_de(erick, sonia).
hermano_de(erick, miguel).
hermano_de(erick, patricia).

hermano_de(miguel, erick).
hermano_de(miguel, luis).
hermano_de(miguel, luis_fernando).
hermano_de(miguel, sonia).
hermano_de(miguel, erick).
hermano_de(miguel, patricia).

hermano_de(patricia, erick).
hermano_de(patricia, luis).
hermano_de(patricia, luis_fernando).
hermano_de(patricia, sonia).
hermano_de(patricia, erick).
hermano_de(patricia, miguel).

% Primos paternos
primo_de(esmeralda, paloma).
primo_de(esmeralda, octavio).
primo_de(paloma, esmeralda).
primo_de(paloma, octavio).
primo_de(octavio, esmeralda).
primo_de(octavio, paloma).

primo_de(arturo, sebastian).
primo_de(arturo, mariana).
primo_de(sebastian, arturo).
primo_de(sebastian, mariana).
primo_de(mariana, arturo).
primo_de(mariana, sebastian).

% Primos maternos
primo_de(mariana, tatiana).
primo_de(mariana, cynthia).
primo_de(tatiana, mariana).
primo_de(tatiana, cynthia).
primo_de(cynthia, mariana).
primo_de(cynthia, tatiana).