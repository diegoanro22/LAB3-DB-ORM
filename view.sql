CREATE VIEW vista_reservas_completas AS
SELECT 
    r.id,
    g.first_name || ' ' || g.last_name AS guest_name,
    rt.name AS room_type,
    rm.room_number,
    r.start_date,
    r.end_date,
    r.status
FROM hotel_reservation r
JOIN hotel_guest g ON r.guest_id = g.id
JOIN hotel_room rm ON r.room_id = rm.id
JOIN hotel_roomtype rt ON rm.room_type_id = rt.id;
