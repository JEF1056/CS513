% menupage(id, menu_id, page_number, image_id, full_height, full_width, uuid)

% Integrity Constraint Violation: id is not a primary key
icv_id_key(ID, menu_id, M1, M2)     :- menupage(ID, M1, _, _, _, _, _), menupage(ID, M2, _, _, _, _, _), M1 < M2.
icv_id_key(ID, page_number, P1, P2) :- menupage(ID, _, P1, _, _, _, _), menupage(ID, _, P2, _, _, _, _), P1 < P2.
icv_id_key(ID, image_id, I1, I2)    :- menupage(ID, _, _, I1, _, _, _), menupage(ID, _, _, I2, _, _, _), I1 < I2.
icv_id_key(ID, full_height, H1, H2) :- menupage(ID, _, _, _, H1, _, _), menupage(ID, _, _, _, H2, _, _), H1 < H2.
icv_id_key(ID, full_height, W1, W2) :- menupage(ID, _, _, _, _, W1, _), menupage(ID, _, _, _, _, W2, _), W1 < W2.
icv_id_key(ID, uuid, U1, U2)        :- menupage(ID, _, _, _, _, _, U1), menupage(ID, _, _, _, _, _, U2), U1 < U2.

