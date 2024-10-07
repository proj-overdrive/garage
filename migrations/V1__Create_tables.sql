CREATE TABLE spot (
      id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
      owner_id VARCHAR(255) NOT NULL,
      address TEXT NOT NULL,
      latitude DOUBLE PRECISION NOT NULL,
      longitude DOUBLE PRECISION NOT NULL
);

CREATE TABLE bookings (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    parking_spot_id UUID NOT NULL,
    user_id VARCHAR(255) NOT NULL,
    start_time TIMESTAMP NOT NULL,
    end_time TIMESTAMP NOT NULL,
    total_price DOUBLE PRECISION NOT NULL,
    booking_status VARCHAR(10) NOT NULL,
    vehicle_license_plate VARCHAR(20),
    CONSTRAINT fk_parking_spot FOREIGN KEY (parking_spot_id) REFERENCES spot(id)
);
